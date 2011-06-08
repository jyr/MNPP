#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file is part of the web2py Web Framework
Copyrighted by Massimo Di Pierro <mdipierro@cs.depaul.edu>
License: LGPLv3 (http://www.gnu.org/licenses/lgpl.html)

Holds:

- SQLFORM: provide a form for a table (with/without record)
- SQLTABLE: provides a table for a set of records
- form_factory: provides a SQLFORM for an non-db backed table

"""

from http import HTTP
from html import XML, SPAN, TAG, A, DIV, UL, LI, TEXTAREA, BR, IMG, SCRIPT
from html import FORM, INPUT, LABEL, OPTION, SELECT
from html import TABLE, THEAD, TBODY, TR, TD, TH
from html import URL as Url
from dal import DAL, Table, Row, CALLABLETYPES
from storage import Storage
from utils import md5_hash
from validators import IS_EMPTY_OR

import urllib
import re
import cStringIO


table_field = re.compile('[\w_]+\.[\w_]+')
widget_class = re.compile('^\w*')

def safe_int(x):
    try:
        return int(x)
    except ValueError:
        return 0

def safe_float(x):
    try:
        return float(x)
    except ValueError:
        return 0

class FormWidget(object):
    """
    helper for SQLFORM to generate form input fields (widget),
    related to the fieldtype
    """

    @staticmethod
    def _attributes(field, widget_attributes, **attributes):
        """
        helper to build a common set of attributes

        :param field: the field involved, some attributes are derived from this
        :param widget_attributes:  widget related attributes
        :param attributes: any other supplied attributes
        """
        attr = dict(
            _id = '%s_%s' % (field._tablename, field.name),
            _class = widget_class.match(str(field.type)).group(),
            _name = field.name,
            requires = field.requires,
            )
        attr.update(widget_attributes)
        attr.update(attributes)
        return attr

    @staticmethod
    def widget(field, value, **attributes):
        """
        generates the widget for the field.

        When serialized, will provide an INPUT tag:

        - id = tablename_fieldname
        - class = field.type
        - name = fieldname

        :param field: the field needing the widget
        :param value: value
        :param attributes: any other attributes to be applied
        """

        raise NotImplementedError

class StringWidget(FormWidget):

    @staticmethod
    def widget(field, value, **attributes):
        """
        generates an INPUT text tag.

        see also: :meth:`FormWidget.widget`
        """

        default = dict(
            _type = 'text',
            value = (value!=None and str(value)) or '',
            )
        attr = StringWidget._attributes(field, default, **attributes)

        return INPUT(**attr)


class IntegerWidget(StringWidget):

    pass


class DoubleWidget(StringWidget):

    pass


class DecimalWidget(StringWidget):

    pass


class TimeWidget(StringWidget):

    pass


class DateWidget(StringWidget):

    pass


class DatetimeWidget(StringWidget):

    pass


class TextWidget(FormWidget):

    @staticmethod
    def widget(field, value, **attributes):
        """
        generates a TEXTAREA tag.

        see also: :meth:`FormWidget.widget`
        """

        default = dict(
            value = value,
            )
        attr = TextWidget._attributes(field, default, **attributes)

        return TEXTAREA(**attr)


class BooleanWidget(FormWidget):

    @staticmethod
    def widget(field, value, **attributes):
        """
        generates an INPUT checkbox tag.

        see also: :meth:`FormWidget.widget`
        """

        default=dict(
            _type='checkbox',
            value=value,
            )
        attr = BooleanWidget._attributes(field, default, **attributes)

        return INPUT(**attr)


class OptionsWidget(FormWidget):

    @staticmethod
    def has_options(field):
        """
        checks if the field has selectable options

        :param field: the field needing checking
        :returns: True if the field has options
        """

        return hasattr(field.requires, 'options')

    @staticmethod
    def widget(field, value, **attributes):
        """
        generates a SELECT tag, including OPTIONs (only 1 option allowed)

        see also: :meth:`FormWidget.widget`
        """
        default = dict(
            value=value,
            )
        attr = OptionsWidget._attributes(field, default, **attributes)

        requires = field.requires
        if not isinstance(requires, (list, tuple)):
            requires = [requires]
        if requires:
            if hasattr(requires[0], 'options'):
                options = requires[0].options()
            else:
                raise SyntaxError, 'widget cannot determine options of %s' \
                    % field
        opts = [OPTION(v, _value=k) for (k, v) in options]

        return SELECT(*opts, **attr)

class ListWidget(StringWidget):
    @staticmethod
    def widget(field,value,**attributes):
        _id = '%s_%s' % (field._tablename, field.name)
        _name = field.name
        if field.type=='list:integer': _class = 'integer'
        else: _class = 'string'
        items=[LI(INPUT(_id=_id,_class=_class,_name=_name,value=v,hideerror=True)) \
                   for v in value or ['']]
        script=SCRIPT("""
// from http://refactormycode.com/codes/694-expanding-input-list-using-jquery
(function(){
jQuery.fn.grow_input = function() {
  return this.each(function() {
    var ul = this;
    jQuery(ul).find(":text").after('<a href="javascript:void(0)>+</a>').keypress(function (e) { return (e.which == 13) ? pe(ul) : true; }).next().click(function(){ pe(ul) });
  });
};
function pe(ul) {
  var new_line = ml(ul);
  rel(ul);
  new_line.appendTo(ul);
  new_line.find(":text").focus();
  return false;
}
function ml(ul) {
  var line = jQuery(ul).find("li:first").clone(true);
  line.find(':text').val('');
  return line;
}
function rel(ul) {
  jQuery(ul).find("li").each(function() {
    var trimmed = jQuery.trim(jQuery(this.firstChild).val());
    if (trimmed=='') jQuery(this).remove(); else jQuery(this.firstChild).val(trimmed);
  });
}
})();
jQuery(document).ready(function(){jQuery('#%s_grow_input').grow_input();});
""" % _id)
        attributes['_id']=_id+'_grow_input'
        return TAG[''](UL(*items,**attributes),script)


class MultipleOptionsWidget(OptionsWidget):

    @staticmethod
    def widget(field, value, size=5, **attributes):
        """
        generates a SELECT tag, including OPTIONs (multiple options allowed)

        see also: :meth:`FormWidget.widget`

        :param size: optional param (default=5) to indicate how many rows must
            be shown
        """

        attributes.update(dict(_size=size, _multiple=True))

        return OptionsWidget.widget(field, value, **attributes)


class RadioWidget(OptionsWidget):

    @staticmethod
    def widget(field, value, **attributes):
        """
        generates a TABLE tag, including INPUT radios (only 1 option allowed)

        see also: :meth:`FormWidget.widget`
        """

        attr = OptionsWidget._attributes(field, {}, **attributes)

        requires = field.requires
        if not isinstance(requires, (list, tuple)):
            requires = [requires]
        if requires:
            if hasattr(requires[0], 'options'):
                options = requires[0].options()
            else:
                raise SyntaxError, 'widget cannot determine options of %s' \
                    % field

        options = [(k, v) for k, v in options if str(v)]
        opts = []
        cols = attributes.get('cols',1)
        totals = len(options)
        mods = totals%cols
        rows = totals/cols
        if mods:
            rows += 1

        for r_index in range(rows):
            tds = []
            for k, v in options[r_index*cols:(r_index+1)*cols]:
                tds.append(TD(INPUT(_type='radio', _name=field.name,
                         requires=attr.get('requires',None),
                         hideerror=True, _value=k,
                         value=value), v))
            opts.append(TR(tds))

        if opts:
            opts[-1][0][0]['hideerror'] = False
        return TABLE(*opts, **attr)


class CheckboxesWidget(OptionsWidget):

    @staticmethod
    def widget(field, value, **attributes):
        """
        generates a TABLE tag, including INPUT checkboxes (multiple allowed)

        see also: :meth:`FormWidget.widget`
        """

        # was values = re.compile('[\w\-:]+').findall(str(value))
        if isinstance(value, (list, tuple)):
            values = [str(v) for v in value]
        else:
            values = [str(value)]

        attr = OptionsWidget._attributes(field, {}, **attributes)

        requires = field.requires
        if not isinstance(requires, (list, tuple)):
            requires = [requires]
        if requires:
            if hasattr(requires[0], 'options'):
                options = requires[0].options()
            else:
                raise SyntaxError, 'widget cannot determine options of %s' \
                    % field

        options = [(k, v) for k, v in options if k != '']
        opts = []
        cols = attributes.get('cols', 1)
        totals = len(options)
        mods = totals % cols
        rows = totals / cols
        if mods:
            rows += 1

        for r_index in range(rows):
            tds = []
            for k, v in options[r_index*cols:(r_index+1)*cols]:
                if str(k).isdigit() and k in values:
                    r_value = k
                else:
                    r_value = []
                tds.append(TD(INPUT(_type='checkbox', _name=field.name,
                         requires=attr.get('requires', None),
                         hideerror=True, _value=k,
                         value=r_value), v))
            opts.append(TR(tds))

        if opts:
            opts[-1][0][0]['hideerror'] = False
        return TABLE(*opts, **attr)


class PasswordWidget(FormWidget):

    DEFAULT_PASSWORD_DISPLAY = 8*('*')

    @staticmethod
    def widget(field, value, **attributes):
        """
        generates a INPUT password tag.
        If a value is present it will be shown as a number of '*', not related
        to the length of the actual value.

        see also: :meth:`FormWidget.widget`
        """

        default=dict(
            _type='password',
            _value=(value and PasswordWidget.DEFAULT_PASSWORD_DISPLAY) or '',
            )
        attr = PasswordWidget._attributes(field, default, **attributes)

        return INPUT(**attr)


class UploadWidget(FormWidget):

    DEFAULT_WIDTH = '150px'
    ID_DELETE_SUFFIX = '__delete'
    GENERIC_DESCRIPTION = 'file'
    DELETE_FILE = 'delete'

    @staticmethod
    def widget(field, value, download_url=None, **attributes):
        """
        generates a INPUT file tag.

        Optionally provides an A link to the file, including a checkbox so
        the file can be deleted.
        All is wrapped in a DIV.

        see also: :meth:`FormWidget.widget`

        :param download_url: Optional URL to link to the file (default = None)
        """

        default=dict(
            _type='file',
            )
        attr = UploadWidget._attributes(field, default, **attributes)

        inp = INPUT(**attr)

        if download_url and value:
            url = download_url + '/' + value
            (br, image) = ('', '')
            if UploadWidget.is_image(value):
                br = BR()
                image = IMG(_src = url, _width = UploadWidget.DEFAULT_WIDTH)

            requires = attr["requires"]
            if requires == [] or isinstance(requires, IS_EMPTY_OR):
                inp = DIV(inp, '[',
                          A(UploadWidget.GENERIC_DESCRIPTION, _href = url),
                          '|',
                          INPUT(_type='checkbox',
                                _name=field.name + UploadWidget.ID_DELETE_SUFFIX),
                          UploadWidget.DELETE_FILE,
                          ']', br, image)
            else:
                inp = DIV(inp, '[',
                          A(UploadWidget.GENERIC_DESCRIPTION, _href = url),
                          ']', br, image)
        return inp

    @staticmethod
    def represent(field, value, download_url=None):
        """
        how to represent the file:

        - with download url and if it is an image: <A href=...><IMG ...></A>
        - otherwise with download url: <A href=...>file</A>
        - otherwise: file

        :param field: the field
        :param value: the field value
        :param download_url: url for the file download (default = None)
        """

        inp = UploadWidget.GENERIC_DESCRIPTION

        if download_url and value:
            url = download_url + '/' + value
            if UploadWidget.is_image(value):
                inp = IMG(_src = url, _width = UploadWidget.DEFAULT_WIDTH)
            inp = A(inp, _href = url)

        return inp

    @staticmethod
    def is_image(value):
        """
        Tries to check if the filename provided references to an image

        Checking is based on filename extension. Currently recognized:
           gif, png, jp(e)g, bmp

        :param value: filename
        """

        extension = value.split('.')[-1].lower()
        if extension in ['gif', 'png', 'jpg', 'jpeg', 'bmp']:
            return True
        return False


class AutocompleteWidget(object):

    def __init__(self, request, field, id_field=None, db=None,
                 orderby=None, limitby=(0,10),
                 keyword='_autocomplete_%(fieldname)s',
                 min_length=2):
        self.request = request
        self.keyword = keyword % dict(fieldname=field.name)
        self.db = db or field._db
        self.orderby = orderby
        self.limitby = limitby
        self.min_length = min_length
        self.fields=[field]
        if id_field:
            self.is_reference = True
            self.fields.append(id_field)
        else:
            self.is_reference = False
        if hasattr(request,'application'):
            self.url = Url(r=request, args=request.args)
            self.callback()
        else:
            self.url = request
    def callback(self):
        if self.keyword in self.request.vars:
            field = self.fields[0]
            rows = self.db(field.like(self.request.vars[self.keyword]+'%'))\
                .select(orderby=self.orderby,limitby=self.limitby,*self.fields)
            if rows:
                if self.is_reference:
                    id_field = self.fields[1]
                    raise HTTP(200,SELECT(_id=self.keyword,_class='autocomplete',
                                          _size=len(rows),_multiple=(len(rows)==1),
                                          *[OPTION(s[field.name],_value=s[id_field.name],
                                                   _selected=(k==0)) \
                                                for k,s in enumerate(rows)]).xml())
                else:
                    raise HTTP(200,SELECT(_id=self.keyword,_class='autocomplete',
                                          _size=len(rows),_multiple=(len(rows)==1),
                                          *[OPTION(s[field.name],
                                                   _selected=(k==0)) \
                                                for k,s in enumerate(rows)]).xml())
            else:

                raise HTTP(200,'')
    def __call__(self,field,value,**attributes):
        default = dict(
            _type = 'text',
            value = (value!=None and str(value)) or '',
            )
        attr = StringWidget._attributes(field, default, **attributes)
        div_id = self.keyword+'_div'
        attr['_autocomplete']='off'
        if self.is_reference:
            key2 = self.keyword+'_aux'
            key3 = self.keyword+'_auto'
            attr['_class']='string'
            name = attr['_name']
            if 'requires' in attr: del attr['requires']
            attr['_name'] = key2
            value = attr['value']
            record = self.db(self.fields[1]==value).select(self.fields[0]).first()
            attr['value'] = record and record[self.fields[0].name]
            attr['_onblur']="jQuery('#%(div_id)s').delay(3000).fadeOut('slow');" % \
                dict(div_id=div_id,u='F'+self.keyword)
            attr['_onkeyup'] = "jQuery('#%(key3)s').val('');var e=event.which?event.which:event.keyCode; function %(u)s(){jQuery('#%(id)s').val(jQuery('#%(key)s :selected').text());jQuery('#%(key3)s').val(jQuery('#%(key)s').val())}; if(e==39) %(u)s(); else if(e==40) {if(jQuery('#%(key)s option:selected').next().length)jQuery('#%(key)s option:selected').attr('selected',null).next().attr('selected','selected'); %(u)s();} else if(e==38) {if(jQuery('#%(key)s option:selected').prev().length)jQuery('#%(key)s option:selected').attr('selected',null).prev().attr('selected','selected'); %(u)s();} else if(jQuery('#%(id)s').val().length>=%(min_length)s) jQuery.get('%(url)s?%(key)s='+escape(jQuery('#%(id)s').val()),function(data){if(data=='')jQuery('#%(key3)s').val('');else{jQuery('#%(id)s').next('.error').hide();jQuery('#%(div_id)s').html(data).show().focus();jQuery('#%(div_id)s select').css('width',jQuery('#%(id)s').css('width'));jQuery('#%(key3)s').val(jQuery('#%(key)s').val());jQuery('#%(key)s').change(%(u)s);jQuery('#%(key)s').click(%(u)s);};}); else jQuery('#%(div_id)s').fadeOut('slow');" % \
                dict(url=self.url,min_length=self.min_length,
                     key=self.keyword,id=attr['_id'],key2=key2,key3=key3,
                     name=name,div_id=div_id,u='F'+self.keyword)
            if self.min_length==0:
                attr['_onfocus'] = attr['_onkeyup']
            return TAG[''](INPUT(**attr),INPUT(_type='hidden',_id=key3,_value=value,
                                               _name=name,requires=field.requires),
                           DIV(_id=div_id,_style='position:absolute;'))
        else:
            attr['_name']=field.name
            attr['_onblur']="jQuery('#%(div_id)s').delay(3000).fadeOut('slow');" % \
                dict(div_id=div_id,u='F'+self.keyword)
            attr['_onkeyup'] = "var e=event.which?event.which:event.keyCode; function %(u)s(){jQuery('#%(id)s').val(jQuery('#%(key)s').val())}; if(e==39) %(u)s(); else if(e==40) {if(jQuery('#%(key)s option:selected').next().length)jQuery('#%(key)s option:selected').attr('selected',null).next().attr('selected','selected'); %(u)s();} else if(e==38) {if(jQuery('#%(key)s option:selected').prev().length)jQuery('#%(key)s option:selected').attr('selected',null).prev().attr('selected','selected'); %(u)s();} else if(jQuery('#%(id)s').val().length>=%(min_length)s) jQuery.get('%(url)s?%(key)s='+escape(jQuery('#%(id)s').val()),function(data){jQuery('#%(id)s').next('.error').hide();jQuery('#%(div_id)s').html(data).show().focus();jQuery('#%(div_id)s select').css('width',jQuery('#%(id)s').css('width'));jQuery('#%(key)s').change(%(u)s);jQuery('#%(key)s').click(%(u)s);}); else jQuery('#%(div_id)s').fadeOut('slow');" % \
                dict(url=self.url,min_length=self.min_length,
                     key=self.keyword,id=attr['_id'],div_id=div_id,u='F'+self.keyword)
            if self.min_length==0:
                attr['_onfocus'] = attr['_onkeyup']
            return TAG[''](INPUT(**attr),DIV(_id=div_id,_style='position:absolute;'))


class SQLFORM(FORM):

    """
    SQLFORM is used to map a table (and a current record) into an HTML form

    given a SQLTable stored in db.table

    generates an insert form::

        SQLFORM(db.table)

    generates an update form::

        record=db.table[some_id]
        SQLFORM(db.table, record)

    generates an update with a delete button::

        SQLFORM(db.table, record, deletable=True)

    if record is an int::

        record=db.table[record]

    optional arguments:

    :param fields: a list of fields that should be placed in the form,
        default is all.
    :param labels: a dictionary with labels for each field, keys are the field
        names.
    :param col3: a dictionary with content for an optional third column
            (right of each field). keys are field names.
    :param linkto: the URL of a controller/function to access referencedby
        records
            see controller appadmin.py for examples
    :param upload: the URL of a controller/function to download an uploaded file
            see controller appadmin.py for examples

    any named optional attribute is passed to the <form> tag
            for example _class, _id, _style, _action, _method, etc.

    """

    # usability improvements proposal by fpp - 4 May 2008 :
    # - correct labels (for points to field id, not field name)
    # - add label for delete checkbox
    # - add translatable label for record ID
    # - add third column to right of fields, populated from the col3 dict

    widgets = Storage(dict(
        string = StringWidget,
        text = TextWidget,
        password = PasswordWidget,
        integer = IntegerWidget,
        double = DoubleWidget,
        decimal = DecimalWidget,
        time = TimeWidget,
        date = DateWidget,
        datetime = DatetimeWidget,
        upload = UploadWidget,
        boolean = BooleanWidget,
        blob = None,
        options = OptionsWidget,
        multiple = MultipleOptionsWidget,
        radio = RadioWidget,
        checkboxes = CheckboxesWidget,
        autocomplete = AutocompleteWidget,
        list = ListWidget,
        ))

    FIELDNAME_REQUEST_DELETE = 'delete_this_record'
    FIELDKEY_DELETE_RECORD = 'delete_record'
    ID_LABEL_SUFFIX = '__label'
    ID_ROW_SUFFIX = '__row'

    def __init__(
        self,
        table,
        record = None,
        deletable = False,
        linkto = None,
        upload = None,
        fields = None,
        labels = None,
        col3 = {},
        submit_button = 'Submit',
        delete_label = 'Check to delete:',
        showid = True,
        readonly = False,
        comments = True,
        keepopts = [],
        ignore_rw = False,
        record_id = None,
        formstyle = 'table3cols',
        buttons = ['submit'],
        **attributes
        ):
        """
        SQLFORM(db.table,
               record=None,
               fields=['name'],
               labels={'name': 'Your name'},
               linkto=URL(r=request, f='table/db/')
        """

        self.ignore_rw = ignore_rw
        self.formstyle = formstyle
        nbsp = XML('&nbsp;') # Firefox2 does not display fields with blanks
        FORM.__init__(self, *[], **attributes)
        ofields = fields
        keyed = hasattr(table,'_primarykey')

        # if no fields are provided, build it from the provided table
        # will only use writable or readable fields, unless forced to ignore
        if fields == None:
            fields = [f.name for f in table if (ignore_rw or f.writable or f.readable) and not f.compute]
        self.fields = fields

        # make sure we have an id
        if self.fields[0] != table.fields[0] and \
                isinstance(table,Table) and not keyed:
            self.fields.insert(0, table.fields[0])

        self.table = table

        # try to retrieve the indicated record using its id
        # otherwise ignore it
        if record and isinstance(record, (int, long, str, unicode)):
            if not str(record).isdigit():
                raise HTTP(404, "Object not found")
            record = table._db(table.id == record).select().first()
            if not record:
                raise HTTP(404, "Object not found")
        self.record = record

        self.record_id = record_id
        if keyed:
            if record:
                self.record_id = dict([(k,record[k]) for k in table._primarykey])
            else:
                self.record_id = dict([(k,None) for k in table._primarykey])
        self.field_parent = {}
        xfields = []
        self.fields = fields
        self.custom = Storage()
        self.custom.dspval = Storage()
        self.custom.inpval = Storage()
        self.custom.label = Storage()
        self.custom.comment = Storage()
        self.custom.widget = Storage()
        self.custom.linkto = Storage()

        for fieldname in self.fields:
            if fieldname.find('.') >= 0:
                continue

            field = self.table[fieldname]
            comment = None

            if comments:
                comment = col3.get(fieldname, field.comment)
            if comment == None:
                comment = ''
            self.custom.comment[fieldname] = comment

            if labels != None and fieldname in labels:
                label = labels[fieldname]
                colon = ''
            else:
                label = field.label
                colon = ': '
            self.custom.label[fieldname] = label

            field_id = '%s_%s' % (table._tablename, fieldname)

            label = LABEL(label, colon, _for=field_id,
                          _id=field_id+SQLFORM.ID_LABEL_SUFFIX)

            row_id = field_id+SQLFORM.ID_ROW_SUFFIX
            if field.type == 'id':
                self.custom.dspval.id = nbsp
                self.custom.inpval.id = ''
                widget = ''
                if record:
                    if showid and 'id' in fields and field.readable:
                        v = record['id']
                        widget = SPAN(v, _id=field_id)
                        self.custom.dspval.id = str(v)
                        xfields.append((row_id,label, widget,comment))
                    self.record_id = str(record['id'])
                self.custom.widget.id = widget
                continue

            if readonly and not ignore_rw and not field.readable:
                continue

            if record:
                default = record[fieldname]
            else:
                default = field.default
                if isinstance(default,CALLABLETYPES):
                    default=default()

            cond = readonly or \
                (not ignore_rw and not field.writable and field.readable)

            if default and not cond:
                default = field.formatter(default)
            dspval = default
            inpval = default

            if cond:

                # ## if field.represent is available else
                # ## ignore blob and preview uploaded images
                # ## format everything else

                if field.represent:
                    inp = field.represent(default)
                elif field.type in ['blob']:
                    continue
                elif field.type == 'upload':
                    inp = UploadWidget.represent(field, default, upload)
                elif field.type == 'boolean':
                    inp = self.widgets.boolean.widget(field, default, _disabled=True)
                else:
                    inp = field.formatter(default)
            elif field.type == 'upload':
                if hasattr(field, 'widget') and field.widget:
                    inp = field.widget(field, default, upload)
                else:
                    inp = self.widgets.upload.widget(field, default, upload)
            elif hasattr(field, 'widget') and field.widget:
                inp = field.widget(field, default)
            elif field.type == 'boolean':
                inp = self.widgets.boolean.widget(field, default)
                if default:
                    inpval = 'checked'
                else:
                    inpval = ''
            elif OptionsWidget.has_options(field):
                if not field.requires.multiple:
                    inp = self.widgets.options.widget(field, default)
                else:
                    inp = self.widgets.multiple.widget(field, default)
                if fieldname in keepopts:
                    inpval = TAG[''](*inp.components)
            elif field.type.startswith('list:'):
                inp = self.widgets.list.widget(field,default)
            elif field.type == 'text':
                inp = self.widgets.text.widget(field, default)
            elif field.type == 'password':
                inp = self.widgets.password.widget(field, default)
                if self.record:
                    dspval = PasswordWidget.DEFAULT_PASSWORD_DISPLAY
                else:
                    dspval = ''
            elif field.type == 'blob':
                continue
            else:
                inp = self.widgets.string.widget(field, default)

            xfields.append((row_id,label,inp,comment))
            self.custom.dspval[fieldname] = dspval or nbsp
            self.custom.inpval[fieldname] = inpval or ''
            self.custom.widget[fieldname] = inp

        # if a record is provided and found, as is linkto
        # build a link
        if record and linkto:
            db = linkto.split('/')[-1]
            for (rtable, rfield) in table._referenced_by:
                if keyed:
                    rfld = table._db[rtable][rfield]
                    query = urllib.quote('%s.%s==%s' % (db,rfld,record[rfld.type[10:].split('.')[1]]))
                else:
#                 <block>
                    query = urllib.quote('%s.%s==%s' % (db,table._db[rtable][rfield],record.id))
                lname = olname = '%s.%s' % (rtable, rfield)
                if ofields and not olname in ofields:
                    continue
                if labels and lname in labels:
                    lname = labels[lname]
                widget = A(lname,
                           _class='reference',
                           _href='%s/%s?query=%s' % (linkto, rtable, query))
                xfields.append((olname.replace('.', '__')+SQLFORM.ID_ROW_SUFFIX,
                                '',widget,col3.get(olname,'')))
                self.custom.linkto[olname.replace('.', '__')] = widget
#                 </block>

        # when deletable, add delete? checkbox
        self.custom.deletable = ''
        if record and deletable:
            widget = INPUT(_type='checkbox',
                            _class='delete',
                            _id=self.FIELDKEY_DELETE_RECORD,
                            _name=self.FIELDNAME_REQUEST_DELETE,
                            )
            xfields.append((self.FIELDKEY_DELETE_RECORD+SQLFORM.ID_ROW_SUFFIX,
                            LABEL(
                                delete_label,
                                _for=self.FIELDKEY_DELETE_RECORD,
                                _id=self.FIELDKEY_DELETE_RECORD+SQLFORM.ID_LABEL_SUFFIX),
                            widget,
                            col3.get(self.FIELDKEY_DELETE_RECORD, '')))
            self.custom.deletable = widget
        # when writable, add submit button
        self.custom.submit = ''
        if (not readonly) and ('submit' in buttons):
            widget = INPUT(_type='submit',
                           _value=submit_button)
            xfields.append(('submit_record'+SQLFORM.ID_ROW_SUFFIX,
                            '', widget,col3.get('submit_button', '')))
            self.custom.submit = widget
        # if a record is provided and found
        # make sure it's id is stored in the form
        if record:
            if not self['hidden']:
                self['hidden'] = {}
            if not keyed:
                self['hidden']['id'] = record['id']

        (begin, end) = self._xml()
        self.custom.begin = XML("<%s %s>" % (self.tag, begin))
        self.custom.end = XML("%s</%s>" % (end, self.tag))
        table = self.createform(xfields)
        self.components = [table]

    def createform(self, xfields):
        if self.formstyle == 'table3cols':
            table = TABLE()
            for id,a,b,c in xfields:
                td_b = self.field_parent[id] = TD(b,_class='w2p_fw')
                table.append(TR(TD(a,_class='w2p_fl'),
                                td_b,
                                TD(c,_class='w2p_fc'),_id=id))
        elif self.formstyle == 'table2cols':
            table = TABLE()
            for id,a,b,c in xfields:
                td_b = self.field_parent[id] = TD(b,_class='w2p_fw',_colspan="2")
                table.append(TR(TD(a,_class='w2p_fl'),
                                TD(c,_class='w2p_fc'),_id=id
                                +'1',_class='even'))
                table.append(TR(td_b,_id=id+'2',_class='odd'))
        elif self.formstyle == 'divs':
            table = TAG['']()
            for id,a,b,c in xfields:
                div_b = self.field_parent[id] = DIV(b,_class='w2p_fw')
                table.append(DIV(DIV(a,_class='w2p_fl'),
                                 div_b,
                                 DIV(c,_class='w2p_fc'),_id=id))
        elif self.formstyle == 'ul':
            table = UL()
            for id,a,b,c in xfields:
                div_b = self.field_parent[id] = DIV(b,_class='w2p_fw')
                table.append(LI(DIV(a,_class='w2p_fl'),
                                div_b,
                                DIV(c,_class='w2p_fc'),_id=id))
        elif type(self.formstyle) == type(lambda:None):
            table = TABLE()
            for id,a,b,c in xfields:
                td_b = self.field_parent[id] = TD(b,_class='w2p_fw')
                newrows = self.formstyle(id,a,td_b,c)
                if type(newrows).__name__ != "tuple":
                    newrows = [newrows]
                for newrow in newrows:
                    table.append(newrow)
        else:
            raise RuntimeError, 'formstyle not supported'
        return table


    def accepts(
        self,
        request_vars,
        session=None,
        formname='%(tablename)s/%(record_id)s',
        keepvalues=False,
        onvalidation=None,
        dbio=True,
        hideerror=False,
        detect_record_change=False,
        ):

        """
        similar FORM.accepts but also does insert, update or delete in DAL.
        but if detect_record_change == True than:
          form.record_changed = False (record is properly validated/submitted)
          form.record_changed = True (record cannot be submitted because changed)
        elseif detect_record_change == False than:
          form.record_changed = None
        """

        if request_vars.__class__.__name__ == 'Request':
            request_vars = request_vars.post_vars

        keyed = hasattr(self.table, '_primarykey')

        # implement logic to detect whether record exist but has been modified
        # server side
        self.record_changed = None
        if detect_record_change:
            if self.record:
                self.record_changed = False
                serialized = '|'.join(str(self.record[k]) for k in self.table.fields())
                self.record_hash = md5_hash(serialized)

        # logic to deal with record_id for keyed tables
        if self.record:
            if keyed:
                formname_id = '.'.join(str(self.record[k])
                                       for k in self.table._primarykey
                                       if hasattr(self.record,k))
                record_id = dict((k, request_vars[k]) for k in self.table._primarykey)
            else:
                (formname_id, record_id) = (self.record.id,
                                            request_vars.get('id', None))
            keepvalues = True
        else:
            if keyed:
                formname_id = 'create'
                record_id = dict([(k, None) for k in self.table._primarykey])
            else:
                (formname_id, record_id) = ('create', None)

        if not keyed and isinstance(record_id, (list, tuple)):
            record_id = record_id[0]

        if formname:
            formname = formname % dict(tablename = self.table._tablename,
                                       record_id = formname_id)

        # ## THIS IS FOR UNIQUE RECORDS, read IS_NOT_IN_DB

        for fieldname in self.fields:
            field = self.table[fieldname]
            requires = field.requires or []
            if not isinstance(requires, (list, tuple)):
                requires = [requires]
            [item.set_self_id(self.record_id) for item in requires
            if hasattr(item, 'set_self_id') and self.record_id]

        # ## END

        fields = {}
        for key in self.vars:
            fields[key] = self.vars[key]

        ret = FORM.accepts(
            self,
            request_vars,
            session,
            formname,
            keepvalues,
            onvalidation,
            hideerror=hideerror,
            )

        if not ret and self.record and self.errors:
            ### if there are errors in update mode
            # and some errors refers to an already uploaded file
            # delete error if
            # - user not trying to upload a new file
            # - there is existing file and user is not trying to delete it
            # this is because removing the file may not pass validation
            for key in self.errors.keys():
                if key in self.table \
                        and self.table[key].type == 'upload' \
                        and request_vars.get(key, None) in (None, '') \
                        and self.record[key] \
                        and not key + UploadWidget.ID_DELETE_SUFFIX in request_vars:
                    del self.errors[key]
            if not self.errors:
                ret = True

        requested_delete = \
            request_vars.get(self.FIELDNAME_REQUEST_DELETE, False)

        self.custom.end = TAG[''](self.hidden_fields(), self.custom.end)

        auch = record_id and self.errors and requested_delete

        # auch is true when user tries to delete a record
        # that does not pass validation, yet it should be deleted

        if not ret and not auch:
            for fieldname in self.fields:
                field = self.table[fieldname]
                ### this is a workaround! widgets should always have default not None!
                if not field.widget and field.type.startswith('list:') and \
                        not OptionsWidget.has_options(field):
                    field.widget = self.widgets.list.widget
                if hasattr(field, 'widget') and field.widget and fieldname in request_vars:
                    if fieldname in self.vars:
                        value = self.vars[fieldname]
                    elif self.record:
                        value = self.record[fieldname]
                    else:
                        value = self.table[fieldname].default
                    row_id = '%s_%s%s' % (self.table, fieldname, SQLFORM.ID_ROW_SUFFIX)
                    widget = field.widget(field, value)
                    self.field_parent[row_id].components = [ widget ]
                    if not field.type.startswith('list:'):
                        self.field_parent[row_id]._traverse(False, hideerror)
                    self.custom.widget[ fieldname ] = widget
            return ret

        if record_id and str(record_id) != str(self.record_id):
            raise SyntaxError, 'user is tampering with form\'s record_id: ' \
                '%s != %s' % (record_id, self.record_id)

        if record_id and dbio:
            if keyed:
                self.vars.update(record_id)
            else:
                self.vars.id = self.record.id

        if requested_delete and self.custom.deletable:
            if dbio:
                if keyed:
                    qry = reduce(lambda x, y: x & y,
                                 [self.table[k] == record_id[k] for k in self.table._primarykey])
                else:
                    qry = self.table.id == self.record.id
                self.table._db(qry).delete()
            self.errors.clear()
            for component in self.elements('input, select, textarea'):
                component['_disabled'] = True
            return True

        for fieldname in self.fields:
            if not fieldname in self.table.fields:
                continue

            if not self.ignore_rw and not self.table[fieldname].writable:
                ### this happens because FORM has no knowledge of writable
                ### and thinks that a missing boolean field is a None
                if self.table[fieldname].type == 'boolean' and \
                    self.vars.get(fieldname, True) == None:
                    del self.vars[fieldname]
                continue

            field = self.table[fieldname]
            if field.type == 'id':
                continue
            if field.type == 'boolean':
                if self.vars.get(fieldname, False):
                    self.vars[fieldname] = fields[fieldname] = True
                else:
                    self.vars[fieldname] = fields[fieldname] = False
            elif field.type == 'password' and self.record\
                and request_vars.get(fieldname, None) == \
                    PasswordWidget.DEFAULT_PASSWORD_DISPLAY:
                continue  # do not update if password was not changed
            elif field.type == 'upload':
                f = self.vars[fieldname]
                fd = '%s__delete' % fieldname
                if f == '' or f == None:
                    if self.vars.get(fd, False) or not self.record:
                        fields[fieldname] = ''
                    else:
                        fields[fieldname] = self.record[fieldname]
                    self.vars[fieldname] = fields[fieldname]
                    continue
                elif hasattr(f, 'file'):
                    (source_file, original_filename) = (f.file, f.filename)
                elif isinstance(f, (str, unicode)):
                    ### do not know why this happens, it should not
                    (source_file, original_filename) = \
                        (cStringIO.StringIO(f), 'file.txt')
                newfilename = field.store(source_file, original_filename)
                # this line is for backward compatibility only
                self.vars['%s_newfilename' % fieldname] = newfilename
                fields[fieldname] = newfilename
                if isinstance(field.uploadfield, str):
                    fields[field.uploadfield] = source_file.read()
                # proposed by Hamdy (accept?) do we need fields at this point?
                self.vars[fieldname] = fields[fieldname]
                continue
            elif fieldname in self.vars:
                fields[fieldname] = self.vars[fieldname]
            elif field.default == None and field.type != 'blob':
                self.errors[fieldname] = 'no data'
                return False
            value = fields.get(fieldname,None)
            if field.type == 'list:string':
                if not isinstance(value, (tuple, list)):
                    fields[fieldname] = value and [value] or []
            elif isinstance(field.type,str) and field.type.startswith('list:'):
                if not isinstance(value, list):
                    fields[fieldname] = [safe_int(x) for x in (value and [value] or [])]
            elif field.type == 'integer':
                if value != None:
                    fields[fieldname] = safe_int(value)
            elif field.type.startswith('reference'):
                if value != None and isinstance(self.table, Table) and not keyed:
                    fields[fieldname] = safe_int(value)
            elif field.type == 'double':
                if value != None:
                    fields[fieldname] = safe_float(value)

        for fieldname in self.vars:
            if fieldname != 'id' and fieldname in self.table.fields\
                 and not fieldname in fields and not fieldname\
                 in request_vars:
                fields[fieldname] = self.vars[fieldname]

        if dbio:
            if 'delete_this_record' in fields:
                # this should never happen but seems to happen to some
                del fields['delete_this_record']
            if keyed:
                if reduce(lambda x, y: x and y, record_id.values()): # if record_id
                    if fields:
                        qry = reduce(lambda x, y: x & y,
                            [self.table[k] == self.record[k] for k in self.table._primarykey])
                        self.table._db(qry).update(**fields)
                else:
                    pk = self.table.insert(**fields)
                    if pk:
                        self.vars.update(pk)
                    else:
                        ret = False
            else:
                if record_id:
                    self.vars.id = self.record.id
                    if fields:
                        self.table._db(self.table.id == self.record.id).update(**fields)
                else:
                    self.vars.id = self.table.insert(**fields)
        return ret

    @staticmethod
    def factory(*fields, **attributes):
        """
        generates a SQLFORM for the given fields.

        Internally will build a non-database based data model
        to hold the fields.
        """
        # Define a table name, this way it can be logical to our CSS.
        # And if you switch from using SQLFORM to SQLFORM.factory
        # your same css definitions will still apply.

        table_name = attributes.get('table_name', 'no_table')

        # So it won't interfear with SQLDB.define_table
        if 'table_name' in attributes:
            del attributes['table_name']

        return SQLFORM(DAL(None).define_table(table_name, *fields), **attributes)


class SQLTABLE(TABLE):

    """
    given a Rows object, as returned by a db().select(), generates
    an html table with the rows.

    optional arguments:

    :param linkto: URL (or lambda to generate a URL) to edit individual records
    :param upload: URL to download uploaded files
    :param orderby: Add an orderby link to column headers.
    :param headers: dictionary of headers to headers redefinions
                    headers can also be a string to gerenare the headers from data
                    for now only headers="fieldname:capitalize",
                    headers="labels" and headers=None are supported
    :param truncate: length at which to truncate text in table cells.
        Defaults to 16 characters.
    :param columns: a list or dict contaning the names of the columns to be shown
        Defaults to all

    Optional names attributes for passed to the <table> tag

    The keys of headers and columns must be of the form "tablename.fieldname"

    Simple linkto example::

        rows = db.select(db.sometable.ALL)
        table = SQLTABLE(rows, linkto='someurl')

    This will link rows[id] to .../sometable/value_of_id


    More advanced linkto example::

        def mylink(field, type, ref):
            return URL(r=request, args=[field])

        rows = db.select(db.sometable.ALL)
        table = SQLTABLE(rows, linkto=mylink)

    This will link rows[id] to
        current_app/current_controlle/current_function/value_of_id


    """

    def __init__(
        self,
        sqlrows,
        linkto=None,
        upload=None,
        orderby=None,
        headers={},
        truncate=16,
        columns=None,
        th_link='',
        **attributes
        ):

        TABLE.__init__(self, **attributes)
        self.components = []
        self.attributes = attributes
        self.sqlrows = sqlrows
        (components, row) = (self.components, [])
        if not sqlrows:
            return
        if not columns:
            columns = sqlrows.colnames
        if headers=='fieldname:capitalize':
            headers = {}
            for c in columns:
                headers[c] = ' '.join([w.capitalize() for w in c.split('.')[-1].split('_')])
        elif headers=='labels':
            headers = {}
            for c in columns:
                (t,f) = c.split('.')
                field = sqlrows.db[t][f]
                headers[c] = field.label

        if headers!=None:
            for c in columns:
                if orderby:
                    row.append(TH(A(headers.get(c, c),
                                    _href=th_link+'?orderby=' + c)))
                else:
                    row.append(TH(headers.get(c, c)))
            components.append(THEAD(TR(*row)))

        tbody = []
        for (rc, record) in enumerate(sqlrows):
            row = []
            if rc % 2 == 0:
                _class = 'even'
            else:
                _class = 'odd'
            for colname in columns:
                if not table_field.match(colname):
                    if "_extra" in record and colname in record._extra:
                        r = record._extra[colname]
                        row.append(TD(r))
                        continue
                    else:
                        raise KeyError("Column %s not found (SQLTABLE)" % colname)
                (tablename, fieldname) = colname.split('.')
                try:
                    field = sqlrows.db[tablename][fieldname]
                except KeyError:
                    field = None
                if tablename in record \
                        and isinstance(record,Row) \
                        and isinstance(record[tablename],Row):
                    r = record[tablename][fieldname]
                elif fieldname in record:
                    r = record[fieldname]
                else:
                    raise SyntaxError, 'something wrong in Rows object'
                r_old = r
                if not field:
                    pass
                elif linkto and field.type == 'id':
                    try:
                        href = linkto(r, 'table', tablename)
                    except TypeError:
                        href = '%s/%s/%s' % (linkto, tablename, r_old)
                    r = A(r, _href=href)
                elif field.type.startswith('reference'):
                    if linkto:
                        ref = field.type[10:]
                        try:
                            href = linkto(r, 'reference', ref)
                        except TypeError:
                            href = '%s/%s/%s' % (linkto, ref, r_old)
                            if ref.find('.') >= 0:
                                tref,fref = ref.split('.')
                                if hasattr(sqlrows.db[tref],'_primarykey'):
                                    href = '%s/%s?%s' % (linkto, tref, urllib.urlencode({fref:r}))
                        if field.represent:
                            r = A(field.represent(r), _href=str(href))
                        else:
                            r = A(str(r), _href=str(href))
                    elif field.represent:
                        r = field.represent(r)
                elif linkto and hasattr(field._table,'_primarykey') and fieldname in field._table._primarykey:
                    # have to test this with multi-key tables
                    key = urllib.urlencode(dict( [ \
                                ((tablename in record \
                                      and isinstance(record, Row) \
                                      and isinstance(record[tablename], Row)) and
                                 (k, record[tablename][k])) or (k, record[k]) \
                                    for k in field._table._primarykey ] ))
                    r = A(r, _href='%s/%s?%s' % (linkto, tablename, key))
                elif field.type.startswith('list:'):
                    r = field.represent(r or [])
                elif field.represent:
                    r = field.represent(r)
                elif field.type == 'blob' and r:
                    r = 'DATA'
                elif field.type == 'upload':
                    if upload and r:
                        r = A('file', _href='%s/%s' % (upload, r))
                    elif r:
                        r = 'file'
                    else:
                        r = ''
                elif field.type in ['string','text']:
                    r = str(field.formatter(r))
                    ur = unicode(r, 'utf8')
                    if truncate!=None and len(ur) > truncate:
                        r = ur[:truncate - 3].encode('utf8') + '...'
                row.append(TD(r))
            tbody.append(TR(_class=_class, *row))
        components.append(TBODY(*tbody))

form_factory = SQLFORM.factory # for backward compatibility, deprecated


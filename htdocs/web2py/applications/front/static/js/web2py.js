function popup(url) {
  newwindow=window.open(url,'name','height=400,width=600');
  if (window.focus) newwindow.focus();
  return false;
}

function collapse(id) { jQuery('#'+id).slideToggle(); }

function fade(id,value) { if(value>0) jQuery('#'+id).hide().fadeIn('slow'); else jQuery('#'+id).show().fadeOut('slow'); }

function ajax(u,s,t) {
  query = '';
  if (typeof s == "string") {
    d = jQuery(s).serialize();
    if(d){ query = d; }
  } else {
    pcs = [];
    for(i=0; i<s.length; i++) {
      q = jQuery("[name="+s[i]+"]").serialize();
      if(q){pcs.push(q);}
    }
    if (pcs.length>0){query = pcs.join("&");}
  }
  jQuery.ajax({type: "POST", url: u, data: query, success: function(msg) { if(t) { if(t==':eval') eval(msg); else jQuery("#" + t).html(msg); } } }); 
}

String.prototype.reverse = function () { return this.split('').reverse().join('');};
function web2py_ajax_init() {
  jQuery('.hidden').hide();
  jQuery('.error').hide().slideDown('slow');
  jQuery('.flash').click(function() { jQuery(this).fadeOut('slow'); return false; });
  jQuery('input.integer').live('keyup', function(){this.value=this.value.reverse().replace(/[^0-9\-]|\-(?=.)/g,'').reverse();});
  jQuery('input.double,input.decimal').live('keyup', function(){this.value=this.value.reverse().replace(/[^0-9\-\.,]|[\-](?=.)|[\.,](?=[0-9]*[\.,])/g,'').reverse();});
  jQuery("input[type='checkbox'].delete").live('click', function(){ if(this.checked) if(!confirm("{{=T('Sure you want to delete this object?')}}")) this.checked=false; });
  try {jQuery("input.date").live('focus',function() {Calendar.setup({
    inputField:this, ifFormat:"{{=T('%Y-%m-%d')}}", showsTime:false
  }); }); } catch(e) {};
  try { jQuery("input.datetime").live('focus', function() {Calendar.setup({
    inputField:this, ifFormat:"{{=T('%Y-%m-%d %H:%M:%S')}}", showsTime: true,timeFormat: "24"
  }); }); } catch(e) {};

  jQuery("input.time").live('focus', function() { var el = jQuery(this); 
    if (!el.hasClass('hasTimeEntry')) try { el.timeEntry(); } catch(e) {}; 
  });
};

jQuery(function() {   
  var flash = jQuery('.flash');
  flash.hide();
  if(flash.html()) flash.slideDown();
  web2py_ajax_init();
});

function web2py_trap_form(action,target) {
  jQuery('#'+target+' form').each(function(i){
    var form=jQuery(this);
    if(!form.hasClass('no_trap'))
    form.submit(function(obj){
      jQuery('.flash').hide().html('');
      web2py_ajax_page('post',action,form.serialize(),target);
      return false;
    });
  });
}

function web2py_ajax_page(method,action,data,target) {
  jQuery.ajax({'type':method,'url':action,'data':data,
    'beforeSend':function(xhr) {
      xhr.setRequestHeader('web2py-component-location',document.location);
      xhr.setRequestHeader('web2py-component-element',target);},
    'complete':function(xhr,text){
      var html=xhr.responseText;
      var content=xhr.getResponseHeader('web2py-component-content'); 
      var command=xhr.getResponseHeader('web2py-component-command');
      var flash=xhr.getResponseHeader('web2py-component-flash');
      var t = jQuery('#'+target);
      if(content=='prepend') t.prepend(html); 
      else if(content=='append') t.append(html);
      else if(content!='hide') t.html(html);  
      web2py_trap_form(action,target);
      web2py_ajax_init();      
      if(command) eval(command);
      if(flash) jQuery('.flash').html(flash).slideDown();
    }
  });
}

function web2py_component(action,target) {
  jQuery(function(){ web2py_ajax_page('get',action,null,target); });
}

function web2py_comet(url,onmessage,onopen,onclose) {
  if ("WebSocket" in window) {
    var ws = new WebSocket(url);
    ws.onopen = onopen?onopen:(function(){});
    ws.onmessage = onmessage;
    ws.onclose = onclose?onclose:(function(){});
    return true; // supported
  } else return false; // not supported
}

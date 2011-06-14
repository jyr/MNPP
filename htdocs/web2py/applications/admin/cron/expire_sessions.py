EXPIRATION_MINUTES=60
DIGITS=('0','1','2','3','4','5','6','7','8','9')
import os, time, stat, logging
path=os.path.join(request.folder,'sessions')
if not os.path.exists(path):
   os.mkdir(path)
now=time.time()
for filename in os.listdir(path):
   fullpath=os.path.join(path,filename)
   try:
      if os.path.isfile(fullpath):
         t=os.stat(fullpath)[stat.ST_MTIME]
         if now-t>EXPIRATION_MINUTES*60 and filename.startswith(DIGITS):
            try:
               os.unlink(fullpath)
            except Exception,e:
               logging.warn('failure to unlink %s: %s' % (fullpath,e))
   except Exception, e:
      logging.warn('failure to stat %s: %s' % (fullpath,e))
         

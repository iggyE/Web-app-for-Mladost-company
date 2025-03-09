from django.contrib import admin
from .models import Glina,Grumen,NeoblikovanCrep,OblikovanCrep,VagonPecenje,VagonSusenje,OsusenCrep,IspecenCrep,PaketCrepa

# Register your models here.
admin.site.register(Glina)
admin.site.register(Grumen)
admin.site.register(NeoblikovanCrep)
admin.site.register(OblikovanCrep)
admin.site.register(VagonSusenje)
admin.site.register(VagonPecenje)
admin.site.register(OsusenCrep)
admin.site.register(IspecenCrep)
admin.site.register(PaketCrepa)


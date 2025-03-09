from django.shortcuts import render,redirect
from .models import Glina,Grumen,NeoblikovanCrep,OblikovanCrep,OsusenCrep,VagonPecenje,VagonSusenje,PaketCrepa,IspecenCrep
from django.contrib import messages

# Create your views here.

def PocetnaView(request):
    return render(request,'pocetna.html')

def KontaktView(request):
    return render(request,'kontakt.html')

def KontaktiView(request):
    return render(request,'kontakti.html')

def NamaView(request):
    return render(request,'nama.html')

def ProizvodnjaView(request):
    return render(request,'proizvodnja.html')

def KoSmoMiView(request):
    return render(request,'kosmomi.html')

def IstorijaView(request):
    return render(request,'istorija.html')

def GdeSeNalazimoView(request):
    return render(request,'gdesenalazimo.html')

def NabavljanjeGlineView(request):
    glina = Glina.objects.first()  

    if request.method == "POST":
        trenutna_kolicina = int(request.POST.get('kolicina', 0))
        glina.kolicina += trenutna_kolicina
        glina.save()

        messages.success(request, f"Uspešno je dodato {trenutna_kolicina} kg gline!")
        messages.success(request, f"Sada raspolažemo sa {glina.kolicina} kilograma gline.")

    context = {'trenutna_kolicina': glina.kolicina if glina else 0}
    return render(request, 'nabavljanjegline.html', context)

def PrimarnaObradaView(request):
    glina = Glina.objects.first()  
    grumen = Grumen.objects.first()  


    if not glina:
        glina = Glina.objects.create(kolicina=0)
    if not grumen:
        grumen = Grumen.objects.create(kolicina=0)

    if request.method == "POST":
        # Dodavanje gline
        trenutna_kolicina_gline = int(request.POST.get('kolicina', 0))
        if trenutna_kolicina_gline > 0:
            glina.kolicina += trenutna_kolicina_gline
            glina.save()
            messages.success(request, f"Uspešno je dodato {trenutna_kolicina_gline} kg gline!")
            messages.success(request, f"Sada raspolažemo sa {glina.kolicina} kg gline.")

        trenutna_kolicina_grumena = int(request.POST.get('kolicina_g', 0))
        if trenutna_kolicina_grumena > 0:
            if glina.kolicina >= trenutna_kolicina_grumena:
                glina.kolicina -= trenutna_kolicina_grumena
                grumen.kolicina_g += trenutna_kolicina_grumena
                glina.save()
                grumen.save()
                messages.success(
                    request,
                    f"Uspešno napravljeno {trenutna_kolicina_grumena} kg grumena! "
                    f"Ostalo je {glina.kolicina} kg gline."
                )
            else:
                messages.error(request, "Nedovoljno gline za ovu preradu.")

    context = {
        'trenutna_kolicina': glina.kolicina,
        'trenutna_kolicina_g': grumen.kolicina_g
    }

    return render(request, 'primarnaobrada.html', context)

def SekundarnaObradaView(request):
    return render(request,'sekundarnaobrada.html')

def OblikovanjeCrepaView(request):
    grumen = Grumen.objects.first()
    neoblikovani_crep = NeoblikovanCrep.objects.first()
    oblikovani_crep = OblikovanCrep.objects.first()

    if request.method == 'POST':
        if 'dodaj_neoblikovane' in request.POST:
            broj_za_dodavanje = int(request.POST.get('broj_neoblikovanih', 0))
            potrebna_kolicina = broj_za_dodavanje * 5

            if grumen.kolicina_g >= potrebna_kolicina:
                neoblikovani_crep.brojN += broj_za_dodavanje
                grumen.kolicina_g -= potrebna_kolicina
                grumen.save()
                neoblikovani_crep.save()
                messages.success(
                    request,
                    f"Uspešno napravljeno {broj_za_dodavanje} neoblikovanih crepova! "
                    f"Ostalo je {grumen.kolicina_g} kg grumena gline."
                )
            else:
                messages.error(request, "Nedovoljno grumena za izradu neoblikovanog crepa!")

        elif 'preradi_u_oblikovane' in request.POST:
            broj_za_preradu = int(request.POST.get('broj_oblikovanih', 0))
            
            if neoblikovani_crep.brojN >= broj_za_preradu:
                neoblikovani_crep.brojN -= broj_za_preradu
                oblikovani_crep.brojO += broj_za_preradu

                povrat_grumena = broj_za_preradu  
                grumen.kolicina_g += povrat_grumena

                grumen.save()
                neoblikovani_crep.save()
                oblikovani_crep.save()
                
                messages.success(
                    request,
                    f"Uspešno preradjeno {broj_za_preradu} oblikovanih crepova! "
                    f"Ostalo je {neoblikovani_crep.brojN} neoblikovanih crepova."
                )
            else:
                messages.error(request, "Nedovoljno grumena za izradu oblikovanog crepa!")

    context = {
        'grumen': grumen,
        'neoblikovani_crep': neoblikovani_crep,
        'oblikovani_crep': oblikovani_crep
    }

    return render(request, 'oblikovanjecrepa.html', context)




def SusenjeSlaganjeView(request):
    oblikovani_crep = OblikovanCrep.objects.first()
    vagon_susenje = VagonSusenje.objects.first()
    osusen_crep = OsusenCrep.objects.first()
    vagon_pecenje = VagonPecenje.objects.first()

    if request.method == "POST":
        if 'dodaj_vagon_susenje' in request.POST:
            broj_vagona = int(request.POST.get('broj_vagona', 0))
            ukupno_potrebno_crepova = broj_vagona * 200

            if oblikovani_crep.brojO >= ukupno_potrebno_crepova:
                oblikovani_crep.brojO -= ukupno_potrebno_crepova
                vagon_susenje.brojVS += broj_vagona
                oblikovani_crep.save()
                vagon_susenje.save()
                
                messages.success(
                    request,
                    f"Uspešno otpremljen {broj_vagona} sa ukupno {oblikovani_crep.brojO} crepa!"
                    f" Ostalo je još{oblikovani_crep.brojO} oblikovanih crepova."
                )
            else:
                messages.error(request, "Nažalost za 1 vagon za sušenje je potrebno 200 oblikovanih crepova!")
                
        elif 'osusi_vagon' in request.POST:
            broj_vagona = int(request.POST.get('broj_vagona', 0))
            
            if vagon_susenje.brojVS >= broj_vagona:
                vagon_susenje.brojVS -= broj_vagona
                osusen_crep.brojOS += broj_vagona * 200
                
                vagon_susenje.save()
                osusen_crep.save()
                
                messages.success(
                    request,
                    f"Uspešno osušenih {broj_vagona} vagona, sada imamo {osusen_crep.brojOS} osušenih crepova!"
                    f" Ostalo je još {vagon_susenje.brojVS} vagona koji nisu osušeni."
                )
            else:
                messages.error(request, "Nemamo nijedan vagon za sušenje!")
            

        elif 'dodaj_vagon_slaganje' in request.POST:
            broj_slaganja = int(request.POST.get('broj_slaganja', 0))

            if broj_slaganja == 40:
                vagon_pecenje.brojVP += 1
                osusen_crep.brojOS -= 200
                
                osusen_crep.save()
                vagon_pecenje.save()
                
                messages.success(
                    request,
                    f"Čestitamo uspešno ste naslagali 40 puta po 5 osušenih crepova!"
                    f" Sada ukupno imamo {vagon_pecenje.brojVP} vagona spremnih za pečenje."
                )
            else:
                messages.error(request, "Morate 40 puta složiti po 5 crepa kako bi na vagonu imali tačno 200 spremnih crepova za pečenje!")
                

    context = {
        'oblikovani_crep': oblikovani_crep,
        'vagon_susenje': vagon_susenje,
        'osusen_crep': osusen_crep,
        'vagon_pecenja': vagon_pecenje
    }
    return render(request, 'susenjeslaganje.html', context)


def PecenjePakovanjeView(request):
    vagon_pecenje = VagonPecenje.objects.first()
    ispecen_crep = IspecenCrep.objects.first()
    paket_crepa = PaketCrepa.objects.first()

    if request.method == "POST":
        if 'ispeci_vagon' in request.POST:
            broj_vagona = int(request.POST.get('broj_vagona', 0))
            ukupno_crepova = broj_vagona * 200

            if vagon_pecenje.brojVP >= broj_vagona:
                vagon_pecenje.brojVP -= broj_vagona
                ispecen_crep.brojIC += ukupno_crepova
                vagon_pecenje.save()
                ispecen_crep.save()
                
                messages.success(
                    request,
                    f"Uspešno ste ispekli {broj_vagona} i sada imate ukupno {ispecen_crep.brojIC} ispečenih crepova!"
                )
            else:
                messages.error(request, "Nažalost nemamo toliko vagona spremnih za pečenje!")
                

        elif 'napravi_paket' in request.POST:
            broj_paketa = int(request.POST.get('broj_paketa', 0))
            ukupno_potrebno_crepova = broj_paketa * 100

            if ispecen_crep.brojIC >= ukupno_potrebno_crepova:
                ispecen_crep.brojIC -= ukupno_potrebno_crepova
                paket_crepa.brojPC += broj_paketa
                ispecen_crep.save()
                paket_crepa.save()
                
                messages.success(
                    request,
                    f"Čestitamo uspešno ste napravili {broj_paketa} gotovih paketa crepa i završili ceo proces proizvodnje! Sada ih imamo ukupno {paket_crepa.brojPC}!"
                )
            else:
                messages.error(request, "Nažalost nemamo toliko ispečenih cigli i ne možemo napraviti paket crepa.")

    context = {
        'vagon_pecenje': vagon_pecenje,
        'ispecen_crep': ispecen_crep,
        'paket_crepa': paket_crepa,
    }
    return render(request, 'pecenjepakovanje.html', context)



def ProbaView(request):
    return render(request,'proba.html')
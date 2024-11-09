def netto(ral):
    imp_irpef=0.9051*ral 
    if imp_irpef <= 15000:
        irpef_lorda=0.2503*imp_irpef
        detraz=1955
        if irpef_lorda>1880:
            renzi=1200
        else:
            renzi=0
    elif imp_irpef <= 28000:
        irpef_lorda=0.2503*15000+0.2538*(imp_irpef-15000)
        detraz=1910*(1+(28000-imp_irpef)/13000)
        renzi=0
    elif imp_irpef <= 50000:
        irpef_lorda=0.2503*15000+0.2538*13000+0.3752*(imp_irpef-28000)
        detraz=1910*(50000-imp_irpef)/22000
        renzi=0
    else:
        irpef_lorda=0.2503*15000+0.2538*13000+0.3752*22000+0.4553*(imp_irpef-50000)
        detraz=0
        renzi=0
    netto_annuo=imp_irpef - irpef_lorda + detraz + renzi
    return netto_annuo

for i in range(14000,52001,2000):
    ran = netto(i)
    cuneo = (i-ran)*100/i
    print("Esempio")
    print("Con una RAL di ",i,"il netto annuo è di ",round(ran,2))
    print("Lo stipendio mensile su 13 mensilità è ",round(ran/13,2))
    print("Il cuneo fiscale e contributivo pesa il ",round(cuneo),"%")
    
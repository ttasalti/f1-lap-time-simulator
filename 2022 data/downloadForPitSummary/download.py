import urllib.request

maps=["brn","ksa","aus","ita","usa","esp","mon","aze","can","gbr","aut","fra","hun","bel","ned","ita","sgp","jpn","usa","mex","bra","uae"]
practices=["first","second","third"]
i=1

for map in maps:
    onlar=str(int(i/10))
    birler=str(i%10)
    pdf_path = "https://www.fia.com/sites/default/files/2022_"+onlar+birler+"_"+map+"_f1_r0"+"_timing_racepitstopsummary_"+"v01.pdf"

    def download_file(download_url, filename):
        response = urllib.request.urlopen(download_url)    
        file = open(filename + ".pdf", 'wb')
        file.write(response.read())
        file.close()
    download_file(pdf_path, onlar+birler+"_"+map+"_"+"racepitstopsummary")
    i+=1
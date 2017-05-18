function makeLogicalPath() {

//
// Bepaal een kruimelpad aan de hand van de directory van de 
// actuele pagina.
// 20040123, Bert van Dijk
//

padString = "";
hyperLink = "";
siteName = "";
oddSite = 0;
heelUrl = String(document.location);

// Strip eventuele parameters eraf

j = heelUrl.indexOf("?");
if ( j != -1) {
   heelUrl = heelUrl.substr(0,j);
}

// heelUrl = heelUrl.replace(/_/g," ");
urlDelen = heelUrl.split("/");
whichSite = urlDelen[2].split(".");

if (whichSite[0] != "www" && whichSite[0] != "www2" && whichSite[0] != "info") {
   oddSite = 1;
   siteName = urlDelen[2];
   urlDelen[2] = "www.knmi.nl";
}

// Bepaal de hyperlink van de document root

hyperLink = urlDelen[0];

j = 1;
while (urlDelen[j] == "" || urlDelen[j].indexOf("knmi.nl") != -1) {
       hyperLink = hyperLink + "/" + urlDelen[j];
       j = j + 1;
}

// Bepaal het bijbehorende item in het kruimelpad en bouw de html

padString = "<a class='kalelink' href='" + hyperLink + "'>";

if (urlDelen[0] == "http:") {
    padString = padString + "Home</a>";
} else
    if (urlDelen[0] == "ftp:") {
        padString = padString + "FTP</a>";
    } else
        if (urlDelen[0] == "file:") {
            padString = "Lokaal"; 
        } else padString = padString + "?</a>";

// Als het niet een van onze websites is, maar een ander systeem, 
// dan zetten we ook een link daar naartoe in het pad

if (oddSite == 1) {
   padString = padString + " <img src='/vinklude/images/pad_pijl.gif' " +
               "border=0 hspace = 0 vspace = 0 valign = middle> " +
               "<a class='kalelink' href='http://" + siteName + "/'>" + whichSite[0] +"</a>";
}


// Kijk of de laatste een filenaam of een lege string is; die moet niet in het pad.
// Sommige mensen zijn te lui om ".html" in te tikken; daarom wordt ook gecheckt
// of er misschien *geen* "/" aan het eind van de URL staat.

k = urlDelen.length;
if (j <= k) {
    if (urlDelen[k-1].indexOf(".") != -1 || urlDelen[k-1] == "" || 
        heelUrl.substr(heelUrl.length-1,1) != "/" ) {
        k = k-1;
    }
}
// Kijk of de laatste "urlDelen" een .html  of anker is of 
// heelUrl eindigt op een "/" : 
// dan moet het logische pad 1 element korter worden.

if (k<urlDelen.length)
  if ( heelUrl.substr(heelUrl.length-1,1) == "/" || urlDelen[k].substr(0,5) == "index" 
       || urlDelen[k].substr(0,1) == "#") k=k-1;

for (var i=j; i < k; i++) {

// Bepaal de hyperlink van het volgende item, en de bijbehorende html

     hyperLink = hyperLink + "/" + urlDelen[i];
     urlDelen[i] = urlDelen[i].replace(/_/g," ");
     padString = padString + " <img src='/vinklude/images/pad_pijl.gif' " +
                 "border=0 hspace = 0 vspace = 0 valign = middle> " +
                 "<a class='kalelink' href='" + hyperLink + "'>" +
                 urlDelen[i] + "</a>";
}

// *** Sluit af met de naam van de huidige pagina, zonder suffix en zonder link
if ( heelUrl[heelUrl.length-1] == "/" ) {
  thispage = urlDelen[k].replace(/_/g," ");
}
else {
  thisindex = Math.min(urlDelen[k].indexOf("."),urlDelen[k].length);
  
  if (thisindex>0) {
    thispage = urlDelen[k].substring(0,thisindex);
    thispage = thispage.replace(/_/g," ");
  }
  else
    thispage = urlDelen[k].replace(/_/g," ");
}

padString = padString + " <img src='/vinklude/images/pad_pijl.gif' " +
                 "border=0 hspace = 0 vspace = 0 valign = middle> " + thispage;
				 
return padString;
}

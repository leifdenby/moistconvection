function pop_sitemap(pagina, hoogte, breedte) {
   var hoog = Math.min(hoogte, 500);
   var breed = Math.min(breedte, 700);
   var bigpic = window.open(pagina, 'sitemap_window', 'toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=1,resizable=1,copyhistory=0,width='+breed+',height='+hoog+'');
   bigpic.focus();
   if (bigpic.opener == null) bigpic.opener = window;
   bigpic.opener.name="pappa";
}



<html>

<head>
  <title>GCSS BLCWG - Model intercomparison webpage</title>
  <META HTTP-EQUIV="CACHE-CONTROL" CONTENT="NO-CACHE">
<meta name="DESCRIPTION" content="RICO">
<meta name="KEYWORDS" content="RICO">

<STYLE TYPE="text/css">
body
   {
//   font-family:"Arial", arial, sans-serif;
//   font-size:10px;
//   font-style:italic;
   color:#7777FF;
   }
a 
   {
//   color:blue;
   cursor:pointer;
   }
   
.indented
   {
   padding-left: 10pt;
   padding-right: 10pt;
   }
.indented2
   {
   padding-left: 20pt;
   padding-right: 20pt;
   }
.indented3
   {
   padding-left: 30pt;
   padding-right: 30pt;
   }
#sidewrapper
   {
   background:#aabbff;
   border:1px solid #ccc;
   margin:5px;
   }   
#sidehome,#sidestandard,#sideinteractive,#sideother,#sidelinks,#sidecontact,#sideconstruct
   {
   background:#bbccff;
   border:1px solid #ddd;
   margin:5px;
   width:230px;
   }   
#mainwrapper
   {
   background:#aabbff;
   border:1px solid #ccc;
   margin:5px;
   }   
</STYLE>



<SCRIPT LANGUAGE="JavaScript">

var col = new String();
var x=1;
 
function blink() {

 if(x%2) {
   col = "rgb(255,0,0)";
 } else {
   col = "rgb(255,255,255)";
   }

 if ( typeof(beta) !== 'undefined' ) {
   beta.style.color=col;x++;if(x>2){x=1};setTimeout("blink()",500);
   }

}

</script>


</head>

<body leftmargin="0" marginwidth="0" topmargin="0" marginheight="0" bgcolor="#99aaff" link="#5555ff" alink="#ffffff" vlink="#5555ff" onload="blink()">

<basefont face="times" color="#000000" size=10>


<!------ Table for top bar ------>
<TABLE WIDTH="1500" HEIGHT="120" BGCOLOR="#aabbff" BORDER="0" CELLSPACING="0" CELLPADDING="0">
<TR>
<TD WIDTH="150">
</TD>
<TD WIDTH="125">
<img src="pics/rainbow.gif" HEIGHT="80"><br>
</TD>
<TD WIDTH="450" ALIGN="LEFT">
<font face=arial color="#5555ff" size=+1><I>
GCSS BLCWG <br>
Model intercomparison webpage
</I></font>
<A TARGET="popup" id="beta" HREF="" onclick="window.open('docs/beta.htm','','width=500,height=400,left=20,top=20');return false" title="This webpage is a Beta-version. Click here for more info" STYLE="color:#FFFFFF;text-decoration:none;padding-left:20pt;" >Beta</A></TD>
<TD WIDTH="300">
</TD>
<TD WIDTH="125">
<img src="pics/EUCLIPSE_logo.png" HEIGHT="80"><br>
</TD>
<TD WIDTH="350">
</TD>
</TR>
</TABLE>


<script type="text/javascript">
<!--
function switchMenu(obj,obj2) {
	var el  = document.getElementById(obj);
	var el2 = document.getElementById(obj2);
	if ( el.style.display != "none") {
	  el.style.display = 'none';
	  el2.value        = 'Off';
	} else {
	  el.style.display = '';
	  el2.value        = 'On';
	}
}
//-->
</script>



<form name="myform" action="selection.php" method="post">



<!------ Big block ------>
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0">
<TR>




<!----- Margin ------------------------>
<TD WIDTH="10" VALIGN="TOP" ALIGN="LEFT">
<TABLE WIDTH="10" BORDER="0" CELLSPACING="0" CELLPADDING="0">
</TABLE>
</TD>




<!----- Side bar ------------------------>
<TD VALIGN="TOP" ALIGN="CENTER">

<br>

<div id="sidewrapper">

<input type="hidden" id="MenuSide" name="MenuSide" value="On">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0">
<TR>
<TD VALIGN="TOP">

<div id="sidewrapperin" >
<TABLE WIDTH="250" BORDER="0" CELLSPACING="0" CELLPADDING="0">

<TR>
<TD WIDTH="250" VALIGN="TOP" ALIGN="CENTER">
<div id="sidehome" STYLE="padding-top:5pt;padding-bottom:5pt;" ALIGN="LEFT">
<I><B><font size=+1 face=arial>
<a href="index.php" title="Back to KPT frontpage" CLASS="indented" STYLE="color:#FFFFFF;text-decoration:none;">Home</a>
</font></B></I>
</div>
</TD>
</TR>

<TR>
<TD WIDTH="250" VALIGN="TOP" ALIGN="CENTER">
<input type="hidden" id="MenuPrefab" name="MenuPrefab" value="Off"><div id="sidestandard" STYLE="padding-top:5pt;padding-bottom:5pt;" ALIGN="LEFT">
<I><B><font size=+1 color="#FFFFFF" face=arial>
<a onclick="switchMenu('sidestandardexpand','MenuPrefab');" title="Expand/Hide" CLASS="indented" STYLE="color:#FFFFFF;text-decoration:none;">Standard output</a>
</font></B></I>
<div id="sidestandardexpand" style="display:none"><p ALIGN="LEFT" CLASS="indented2"><font color="#000000">
Prefabricated plots</p>
<p ALIGN="LEFT" CLASS="indented3"><input type="submit" value="Prefab" name="menu"></p>
</div>
</div>
</TD>
</TR>

<TR>
<TD WIDTH="250" VALIGN="TOP" ALIGN="CENTER">
<input type="hidden" id="MenuInter" name="MenuInter" value="Off"><div id="sideinteractive" STYLE="padding-top:5pt;padding-bottom:5pt;" ALIGN="LEFT">
<I><B><font size=+1 color="#FFFFFF" face=arial>
<a onclick="switchMenu('sideinteractiveexpand','MenuInter');" title="Expand/Hide" CLASS="indented" STYLE="color:#FFFFFF;text-decoration:none;">Interactive interface</a>
</font></B></I>
<div id="sideinteractiveexpand" style="display:none"><p ALIGN="LEFT" CLASS="indented2"><font color="#000000">
Freely combining datastreams</p>
<p ALIGN="LEFT" CLASS="indented3"><input type="submit" value="Timeseries" name="menu"></p>
<p ALIGN="LEFT" CLASS="indented3"><input type="submit" value="Scatter" name="menu"></p>
<p ALIGN="LEFT" CLASS="indented3"><input type="submit" value="Profiles" name="menu"></p>
<p ALIGN="LEFT" CLASS="indented3"><input type="submit" value="Contour" name="menu"></p>
<br>
</div>
</div>
</TD>
</TR>

<TR>
<TD WIDTH="250" VALIGN="TOP" ALIGN="CENTER">
<input type="hidden" id="MenuResource" name="MenuResource" value="Off"><div id="sideother" STYLE="padding-top:5pt;padding-bottom:5pt;" ALIGN="LEFT">
<I><B><font size=+1 color="#FFFFFF" face=arial>
<a onclick="switchMenu('sideotherexpand','MenuResource');" title="Expand/Hide" CLASS="indented" STYLE="color:#FFFFFF;text-decoration:none;">Resources</a>
</font></B></I>
<div id="sideotherexpand" style="display:none"><p ALIGN="LEFT" CLASS="indented2"><A TARGET="popup" HREF="" onclick="window.open('docs/moreinfo.htm','','width=600,height=600,left=20,top=20');return false" >Documentation</A></p>
<p ALIGN="LEFT" CLASS="indented2"><A TARGET="popup" HREF="" onclick="window.open('archive/model/simchart.php','','width=900,height=800,left=20,top=20,scrollbars=1');return false" >Simulation chart</A></p>
<p ALIGN="LEFT" CLASS="indented2"><A TARGET="popup" HREF="" onclick="window.open('labels.php','','width=900,height=600,left=20,top=20,scrollbars=1');return false" >Colors and labels</A></p>
<p ALIGN="LEFT" CLASS="indented2"><A TARGET="popup" HREF="" onclick="window.open('plots/collection_591dd290d0d27/collection.php','','width=1120,height=800,left=20,top=20,scrollbars=1');return false">View plot collection</A></p>
<br>
</div>
</div>
</TD>
</TR>

<TR>
<TD WIDTH="250" VALIGN="TOP" ALIGN="CENTER">
<input type="hidden" id="MenuLinks" name="MenuLinks" value="Off"><div id="sidelinks" STYLE="padding-top:5pt;padding-bottom:5pt;" ALIGN="LEFT">
<I><B><font size=+1 color="#FFFFFF" face=arial>
<a onclick="switchMenu('sidelinksexpand','MenuLinks');" title="Expand/Hide" CLASS="indented" STYLE="color:#FFFFFF;text-decoration:none;">Links</a>
</font></B></I>
<div id="sidelinksexpand" style="display:none"><p ALIGN="LEFT" CLASS="indented">
<A HREF="http://www.gewex.org/gcss.html">GCSS</A>
</p>
<p ALIGN="LEFT" CLASS="indented">
<A HREF="http://www.convection.info/blclouds/">GCSS BLCWG</A>
</p>
<p ALIGN="LEFT" CLASS="indented">
<A HREF="http://cfmip.metoffice.com/">CFMIP</A>
</p>
<p ALIGN="LEFT" CLASS="indented">
<A HREF="http://www.knmi.nl/samenw/euclipse/">EUCLIPSE</A>
</p>
<p ALIGN="LEFT" CLASS="indented">
<A HREF="http://www.knmi.nl/~neggers/KPT">KPT</A>
</p>
<br>
</div>
</div>
</TD>
</TR>

<TR>
<TD WIDTH="250" VALIGN="TOP" ALIGN="CENTER">
<input type="hidden" id="MenuContact" name="MenuContact" value="Off"><div id="sidecontact" STYLE="padding-top:5pt;padding-bottom:5pt;" ALIGN="LEFT">
<I><B><font size=+1 color="#FFFFFF" face=arial>
<a onclick="switchMenu('sidecontactexpand','MenuContact');" title="Expand/Hide" CLASS="indented" STYLE="color:#FFFFFF;text-decoration:none;">Contact</a>
</font></B></I>
<div id="sidecontactexpand" style="display:none"><p ALIGN="LEFT" CLASS="indented2">
<font color="#000000">Email: </font>
<A href="mailto:siebesma@knmi.nl">Pier Siebesma</A>
</p>
<p ALIGN="LEFT" CLASS="indented2">
<font color="#000000">Email: </font>
<A href="mailto:neggers@knmi.nl">Roel Neggers</A>
</p>
<br>
</div>
</div>
</TD>
</TR>


<TR>
<TD HEIGHT="100">
</TD>
</TR>

</TABLE>

</div>

</TD>


<!-- Buttons -->
<TD VALIGN="top" CLASS="indented">
<br>

<TABLE WIDTH="35" BORDER="0" CELLSPACING="0" CELLPADDING="0">
<TR>
<TD>
<img src="pics/buttons/green/2.gif" width="15" height="15" STYLE="cursor:pointer;" onclick="switchMenu('sidewrapperin','MenuSide');" title="Expand Menu">
<img src="pics/buttons/red/1.gif" width="15" height="15" STYLE="cursor:pointer;" onclick="switchMenu('sidewrapperin','MenuSide');" title="Hide Menu">
</TD>
</TR>
</TABLE>

<br>

</TD>


</TR>
</TABLE>
</div>

</TD>






<!----- Boundary ------------------------>
<TD WIDTH="10" VALIGN="TOP" ALIGN="LEFT">
<TABLE WIDTH="10" BORDER="0" CELLSPACING="0" CELLPADDING="0">
</TABLE>
</TD>




<!----- Main area ------------------------>
<TD VALIGN="TOP" ALIGN="LEFT">

<br>

<div id="mainwrapper" CLASS="indented">

<input type="hidden" id="MenuMain" name="MenuMain" value="On">


<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0">
<TR>
<TD VALIGN="TOP">

<TABLE WIDTH="750" BORDER="0" CELLSPACING="0" CELLPADDING="0">
<TR>
<TD colspan="5" HEIGHT="60" ALIGN="CENTER" VALIGN="CENTER">
<I><B><font size=+1 color="#FFFFFF" face=arial>Welcome</font></B></I>
</TD>
</TR>
</TABLE>

<div id="mainwrapperin" >

<TABLE WIDTH="800" BORDER="0" CELLSPACING="0" CELLPADDING="0">

<TR>
<TD COLSPAN=4 WIDTH="750" VALIGN="TOP">
<p align=left CLASS="indented"> 
<font color="#000000">
Welcome to the model intercomparison webpage of the Boundary Layer Cloud Working Group (BLCWG) of the GEWEX Cloud System Studies (GCSS).
</font>
</p>
<p align=left CLASS="indented"> 
<font color="#000000">
Click on "Standard output" to view ready-made plots, or "Interactive interface" to start plotting datastreams interactively. A brief visual instruction on how to use this interface can be found under "Resources/Documentation" in the menu on the left. Various other handy tools available under "Resources" include a simulation chart and a plot collection manager.
</font>
</p>
<p align=left CLASS="indented">
<font color="#000000">
(Hint: if your screen is not wide enough, just hide the menu)
</font>
</p>
<br>
</TD>
</TR>

<TR>
<TD COLSPAN=4 WIDTH="750" HEIGHT="170" VALIGN="TOP" ALIGN="CENTER">
<img src="pics/rico_logo_med.jpg" HEIGHT="150" >
</TD>
</TR>

<TR>
<TD COLSPAN=4 WIDTH="750" HEIGHT="170" VALIGN="TOP" ALIGN="CENTER">
<img src="pics/Magelogo.jpg" HEIGHT="150" >
</TD>
</TR>

<TR>
<TD COLSPAN=4 WIDTH="750" HEIGHT="170" VALIGN="TOP" ALIGN="CENTER">
<img src="pics/trans_02.jpg" HEIGHT="150" >
</TD>
</TR>

<TR>
<TD COLSPAN=4 HEIGHT="100" >
<p align=left CLASS="indented">
<font face=arial color="#ffffff" size=-1><I>
Created by <a href="mailto:Roel.Neggers@knmi.nl">Roel Neggers</a>
</I></font>
</p>

</TD>
</TR>


</TABLE>




</div>  <!-- mainwrapperin -->

</TD>


<!-- Buttons -->
<TD VALIGN="top">
<br>

<TABLE WIDTH="35" BORDER="0" CELLSPACING="0" CELLPADDING="0">
<TR>
<TD>
<img src="pics/buttons/green/2.gif" width="15" height="15" STYLE="cursor:pointer;" onclick="switchMenu('mainwrapperin','MenuMain');" title="Expand Desktop">
<img src="pics/buttons/red/1.gif" width="15" height="15" STYLE="cursor:pointer;" onclick="switchMenu('mainwrapperin','MenuMain');" title="Hide Desktop">
</TD>
</TR>
</TABLE>

<br>

</TD>


</TR>
</TABLE>

</div>  <!-- mainwrapper -->



</TD>
</TR>
</TABLE>


 
</form><br>





</body>

</html>

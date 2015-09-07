#! /usr/bin/python

import cgi 
import cgitb
cgitb.enable()

import csv
Top_HTML = '''<!DOCTYPE html>
<html>
<head>
<link href='http://fonts.googleapis.com/css?family=Oswald' rel='stylesheet' type='text/css'>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
<style>'''

styling1='''
body {
background-image:url('http://newyorktotal.com/wp-content/uploads/2015/04/new_york-hotels.jpg');
background-size: 100%;
background-repeat: repeat-y;
margin: 0;
padding: 0;
}
h1{
color: #004739;
font-family: 'Oswald', sans-serif;
font-weight: bold;
}
div.transbox{
  margin-left: auto;
  margin-right: auto;
  margin-top: 50px;
  height: 90%;
  width: 72%;
  background-color: #ffffff;
  z-index: -1;
  border: 1px solid black;
  opacity:0.7;
  filter:alpha(opacity=40);
}
div.transbox p{
  margin: 5%;
  z-index: -1;
  font-weight: bold;
  color: #FFFFFF;
  
}
body{
    color: #000066;
    font-weight: bold;
    font-family: 'Oswald', sans-serif;
}
img{
    margin-left: auto;
    margin-right: auto;
  height: 20%;
  width: 100%;
}
.button{
 text-decoration:none; text-align:center; 
 padding:10px 30px; 
 border:none;
  
 font:18px 'Oswald', sans-serif;
 color:#E5FFFF; 
 background-color:#3BA4C7; 
 background-image: -moz-linear-gradient(top, #3BA4C7 0%, #1982A5 100%); 
 background-image: -webkit-linear-gradient(top, #3BA4C7 0%, #1982A5 100%); 
 background-image: -o-linear-gradient(top, #3BA4C7 0%, #1982A5 100%); 
 background-image: -ms-linear-gradient(top, #3BA4C7 0% ,#1982A5 100%); 
 filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#1982A5', endColorstr='#1982A5',GradientType=0 ); 
 background-image: linear-gradient(top, #3BA4C7 0% ,#1982A5 100%);   
 -webkit-box-shadow:0px 0px 2px #bababa, inset 0px 0px 1px #ffffff; 
 -moz-box-shadow: 0px 0px 2px #bababa,  inset 0px 0px 1px #ffffff;  
 box-shadow:0px 0px 2px #bababa, inset 0px 0px 1px #ffffff;  
 opacity:0.94; 
 -ms-filter: progid:DXImageTransform.Microsoft.Alpha(Opacity=94); 
 filter: alpha(opacity=94); 
  }.button:hover{
 padding:12px 34px; 
 border:none; 
 
 font:18px 'Oswald', sans-serif;
 color:#E5FFFF; 
 background-color:#3BA4C7; 
 background-image: -moz-linear-gradient(top, #3BA4C7 0%, #1982A5 100%); 
 background-image: -webkit-linear-gradient(top, #3BA4C7 0%, #1982A5 100%); 
 background-image: -o-linear-gradient(top, #3BA4C7 0%, #1982A5 100%); 
 background-image: -ms-linear-gradient(top, #3BA4C7 0% ,#1982A5 100%); 
 filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#1982A5', endColorstr='#1982A5',GradientType=0 ); 
 background-image: linear-gradient(top, #3BA4C7 0% ,#1982A5 100%);   
 -webkit-box-shadow:0px 3px 7px #04626b;  -moz-box-shadow: 0px 3px 7px #04626b;  box-shadow:0px 3px 7px #04626b;  
 opacity:0.85; 
 -ms-filter: progid:DXImageTransform.Microsoft.Alpha(Opacity=85); 
 filter: alpha(opacity=85); 
 }.button:active{
 padding:12px 34px; 
 border:none; 
 
 font:18px 'Oswald', sans-serif;
 color:#E5FFFF; 
 background-color:#3BA4C7; 
 background-image: -moz-linear-gradient(top, #3BA4C7 0%, #1982A5 100%); 
 background-image: -webkit-linear-gradient(top, #3BA4C7 0%, #1982A5 100%); 
 background-image: -o-linear-gradient(top, #3BA4C7 0%, #1982A5 100%); 
 background-image: -ms-linear-gradient(top, #3BA4C7 0% ,#1982A5 100%); 
 filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#1982A5', endColorstr='#1982A5',GradientType=0 ); 
 background-image: linear-gradient(top, #3BA4C7 0% ,#1982A5 100%);   
 -webkit-box-shadow:0px 0px 2px #bababa, inset 0px 0px 1px #ffffff; 
 -moz-box-shadow: 0px 0px 2px #bababa,  inset 0px 0px 1px #ffffff;  
 box-shadow:0px 0px 2px #bababa, inset 0px 0px 1px #ffffff;  
 opacity:0.94; 
 -ms-filter: progid:DXImageTransform.Microsoft.Alpha(Opacity=94); 
 filter: alpha(opacity=94); 
}

td { 
    padding: 7px;
    font-size: 17px;
}
th {
    padding: 10px;
    tetx-align: center;
    font-size: 20px;
}

a:link{
 color: #00B26B;
 }
 a:visited{
 color:#A3CC29;
 }
.back-to-top {
background: none;
margin: 0;
position: fixed;
bottom: 30px;
right: 20px;
width: 150px;
height: 40px;
font-size: 18px;
padding: 0.5em;
text-align: center;
z-index: 100;
color: #CCFFFF;
background-color: #006666;
}
div.maps {
        height: 200px;
        width: 200px;
        margin-left: auto;
        margin-right: auto;
        padding: 0px
}
</style>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/2.0.0/jquery.min.js"></script>
'''

maps2='''
}

google.maps.event.addDomListener(window, 'load', initialize);

    </script>'''

styling2='''
<nav class="navbar navbar-inverse navbar-fixed-top">
  <div class="container-fluid">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="Destinations.html">I &hearts; NY </a>
    </div>

    <!-- Collect the nav links, forms, and other content for toggling -->
      <ul class="nav navbar-nav navbar-right">
        <li><a href="http://www.accuweather.com/en/us/new-york-ny/10007/weather-forecast/349727" target="_blank">Check the weather &#9730;</a></li>
        <li><a href="http://web.mta.info/maps/submap.html" target="_blank">Subway</a></li>
        <li><a href="http://newyork.seriouseats.com" target="_blank">Food</a></li>
        <li><a href="TopHotels.html" target="_blank">Top 3 Hotels</a></li>
        <li><a href="TopTourists.html" target="_blank">Top 3 Attractions</a></li> 
      </ul>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>
</head>
<body>
<div class="transbox">
<h1><center>Lists of Hotel Spots</center></h1>
<hr>

<center>
<table cellpadding='7px' border='1'>
'''

 
Bottom_HTML='''</table>
<br><br><br>
<div class="navbar navbar-inverse navbar-fixed-bottom">
  <div class="navbar-header">
    <a class="navbar-brand" href="Hotel_Spots">Back
    </a>
  </div>
</div>
</div></center>

<a href="#" class="back-to-top"> Back to Top </a>
<script>
jQuery(document).ready(function() {
    var offset = 300;
    var duration = 500;
    jQuery(window).scroll(function() {
        if (jQuery(this).scrollTop() > offset) {
            jQuery('.back-to-top').fadeIn(duration);
        } else {
            jQuery('.back-to-top').fadeOut(duration);
        }
    });
    
    jQuery('.back-to-top').click(function(event) {
        event.preventDefault();
        jQuery('html, body').animate({scrollTop: 0}, duration);
        return false;
    })
});
</script>
</body></html>'''

def SortData(which_region, which_county,which_tag): 
    # read the file and split into lines...
    f=open('nychotels.csv','r')
    s=csv.reader(f)
    field=[]

    #create a list with sublists for each places containing its info
    for i in s:
        field+=i
    field_list=[]
    for d in range(len(field)/12):
        start=d*12
        end=(d+1)*12
        r=field[start:end]
        field_list+=[r]
    field_list=field_list[1:]

    #create a list with all places that satisfies the requirement
    regions=[] 
    for i in field_list:
        if i[0] == which_region:
            if i[1].replace(' ','') == which_county:
                if which_tag in i[8]:
                    name=i[2]
                    punc=" ,.&!@#$%^*()_-+=[]{}\|~'`<>?/1234567890"
                    for c in punc:
                        name=name.replace(c,'')
                    Opt=name+"Opt"
                    _map=name+"_map"
                    _mark=name+"_mark"
                    _id=name+"_id"
                    i.append('''
    var '''+name+" = new google.maps.LatLng"+i[11]+''';
    var '''+Opt+''' = {
   zoom: 15,
   center: '''+name+'''
    }
   var '''+_map+''' = new google.maps.Map(document.getElementById("'''+_id+'''"),
   '''+Opt+''');
   var '''+_mark+''' = new google.maps.Marker({
       position: '''+name+''', 
       map: '''+_map+'''
    });''')
                    regions.append(i)

    #in case no places satisfy requirements
    result= ''
    maps='''<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCVlCUFHTPW_1WwBzOwoI8LJpH5AnVUtyE"></script>'''
    if len(regions)<1:
        result+= '<tr><th>Oops, no tourist spots satisfy your requirement.</th></tr>'
    else:
        maps+='''<script> function initialize() {'''
        for k in regions:
            _id=k[2]
            punc=" ,.&!@#$%^*()_-+=[]{}\|~'`<>?/1234567890"
            for i in punc:
                _id=_id.replace(i,'')
            _id=_id+"_id"
            
            #add clickable link to name of place
            if k[3]!='':
                result+='<tr><th><a href="'+k[3]+'">'+k[2]+'</a></th>'
            #if no website, just add name
            else:
                result+='<tr><th>'+k[2]+'</th>'
            #add descriptions
            result+= '<td>'+k[5]+'</td>'
            #add maps
            result+='<td><div class=maps id="'+_id+'"></div></td></tr>'
            #add to style section
            maps+=k[12]
    return [maps]+[result]

def Step2():
    elements = cgi.FieldStorage()
    a=elements.getvalue('Region')
    b=elements.getvalue('County')
    c=elements.getvalue('tag')
    #get info of maps and result from SortData
    pool=SortData(a, b, c)
    maps=pool[0]
    table=pool[1]
    print 'Content-type: text/html\n\n'
    print Top_HTML
    print styling1
    print maps
    print maps2
    print styling2
    print table
    print Bottom_HTML

Step2()


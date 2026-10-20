(function(){
var d=document.documentElement;
if(!d.getAttribute("data-lang")){
d.setAttribute("data-lang","ja");
try{if(new URLSearchParams(location.search).get("lang")==="en"){var p=location.pathname;location.replace("/en"+(p==="/"?"/":p));return}}catch(e){}
}
document.addEventListener("DOMContentLoaded",function(){
var s=document.getElementById("langsel");
if(s)s.addEventListener("change",function(){location.href=this.value});
});
})();

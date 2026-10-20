(function(){
try{if("serviceWorker" in navigator&&location.protocol==="https:")navigator.serviceWorker.register("/sw.js")}catch(e){}
var K="pm_recent",h=document.documentElement,L=(h.getAttribute("data-lang")||h.getAttribute("lang")||"ja").slice(0,2);
var T={ja:"最近使ったツール",en:"Recently used",zh:"最近使用",es:"Usados recientemente"};
function get(){try{return JSON.parse(localStorage.getItem(K)||"[]")}catch(e){return[]}}
document.addEventListener("DOMContentLoaded",function(){
if(document.getElementById("next")){try{var m=location.pathname.match(/([a-z0-9-]+)\.html$/);if(m){var a=get().filter(function(x){return x!==m[1]});a.unshift(m[1]);localStorage.setItem(K,JSON.stringify(a.slice(0,4)))}}catch(e){}}
var pop=document.querySelector("nav.pop");if(!pop)return;var r=get(),links=[];
r.forEach(function(sl){var c=document.querySelector('.cats a.tool[href$="/'+sl+'.html"]');if(c){var b=c.querySelector("b");links.push('<a href="'+c.getAttribute("href")+'">'+(b?b.innerHTML:sl)+'</a>')}});
if(!links.length)return;var n=document.createElement("nav");n.className="pop recent";n.innerHTML="<b>"+(T[L]||T.ja)+"</b>"+links.join("");pop.parentNode.insertBefore(n,pop)});
})();

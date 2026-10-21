(function(){
try{if("serviceWorker" in navigator&&location.protocol==="https:")navigator.serviceWorker.register("/sw.js")}catch(e){}
var K="pm_recent",h=document.documentElement,L=(h.getAttribute("data-lang")||h.getAttribute("lang")||"ja").slice(0,2);
var T={ja:"最近使ったツール",en:"Recently used",zh:"最近使用",es:"Usados recientemente",ko:"최근 사용한 도구",pt:"Usadas recentemente",fr:"Utilisés récemment",id:"Baru digunakan"};var CK='<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/></svg>';
function get(){try{return JSON.parse(localStorage.getItem(K)||"[]")}catch(e){return[]}}
document.addEventListener("DOMContentLoaded",function(){
if(document.getElementById("next")){try{var m=location.pathname.match(/([a-z0-9-]+)\.html$/);if(m){var a=get().filter(function(x){return x!==m[1]});a.unshift(m[1]);localStorage.setItem(K,JSON.stringify(a.slice(0,4)))}}catch(e){}}
var pop=document.querySelector("nav.pop");if(!pop)return;var r=get(),links=[];
r.forEach(function(sl){var c=document.querySelector('.cats a.tool[href$="/'+sl+'.html"]');if(c){var b=c.querySelector("b");var sv=c.querySelector(".ic svg");links.push('<a href="'+c.getAttribute("href")+'">'+(sv?sv.outerHTML.replace("<svg",'<svg class="pi"'):"")+(b?b.innerHTML:sl)+'</a>')}});
if(!links.length)return;var n=document.createElement("nav");n.className="pop recent";n.innerHTML="<b>"+CK+(T[L]||T.ja)+"</b>"+links.join("");pop.parentNode.insertBefore(n,pop)});
})();

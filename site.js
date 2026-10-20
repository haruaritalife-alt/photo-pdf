(function(){
var d=document.documentElement,pre=d.getAttribute("data-lang"),multi=(pre==="zh"||pre==="es"),l="ja";
if(!multi){
try{var q=new URLSearchParams(location.search).get("lang");
if(q==="en"||q==="ja"){l=q;try{localStorage.setItem("lang",l)}catch(e){}}
else if(localStorage.getItem("lang")==="en")l="en"}catch(e){}
d.setAttribute("data-lang",l);
}
var jaTitle=null,jaDesc=null;
function meta(n){return document.querySelector('meta[name="'+n+'"]')}
function sync(x){var s=document.getElementById("langsel");if(!s)return;for(var i=0;i<s.options.length;i++){var v=s.options[i].value;if(v.indexOf("?lang="+x)>-1&&!multi){s.selectedIndex=i}}}
function apply(x,save){
  d.setAttribute("data-lang",x);
  if(jaTitle===null){jaTitle=document.title;var dm=meta("description");jaDesc=dm?dm.getAttribute("content"):""}
  var te=meta("title-en"),de=meta("desc-en"),dm2=meta("description");
  if(x==="en"){if(te)document.title=te.content;if(dm2&&de)dm2.setAttribute("content",de.content)}
  else{document.title=jaTitle;if(dm2)dm2.setAttribute("content",jaDesc)}
  var bs=document.querySelectorAll(".lang button");
  for(var i=0;i<bs.length;i++)bs[i].setAttribute("aria-pressed",bs[i].getAttribute("data-l")===x?"true":"false");
  sync(x);
  if(save){try{localStorage.setItem("lang",x)}catch(e){}}
}
document.addEventListener("DOMContentLoaded",function(){
  var bs=document.querySelectorAll(".lang button");
  for(var i=0;i<bs.length;i++)bs[i].addEventListener("click",function(){apply(this.getAttribute("data-l"),true)});
  var s=document.getElementById("langsel");
  if(s)s.addEventListener("change",function(){
    var v=this.value,m=v.match(/\?lang=(ja|en)$/);
    if(m&&!multi&&v.split("?")[0]===location.pathname){apply(m[1],true)}else{location.href=v}
  });
  if(!multi)apply(l,false);
});
})();

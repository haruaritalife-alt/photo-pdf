(function(){
try{if("serviceWorker" in navigator&&location.protocol==="https:")navigator.serviceWorker.register("/sw.js")}catch(e){}
var K="pm_recent",h=document.documentElement,L=(h.getAttribute("data-lang")||h.getAttribute("lang")||"ja").slice(0,2);
var T={ja:"最近使ったツール",en:"Recently used",zh:"最近使用",es:"Usados recientemente",ko:"최근 사용한 도구",pt:"Usadas recentemente",fr:"Utilisés récemment",id:"Baru digunakan",vi:"Dùng gần đây",it:"Usati di recente",ru:"Недавно использованные",tr:"Son kullanılanlar",de:"Zuletzt verwendet",hi:"हाल में इस्तेमाल किए"};var CK='<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/></svg>';
function get(){try{return JSON.parse(localStorage.getItem(K)||"[]")}catch(e){return[]}}
document.addEventListener("DOMContentLoaded",function(){
if(document.getElementById("next")){try{var m=location.pathname.match(/([a-z0-9-]+)\.html$/);if(m){var a=get().filter(function(x){return x!==m[1]});a.unshift(m[1]);localStorage.setItem(K,JSON.stringify(a.slice(0,4)))}}catch(e){}}
var pop=document.querySelector("nav.pop");if(!pop)return;var r=get(),links=[];
r.forEach(function(sl){var c=document.querySelector('.cats a.tool[href$="/'+sl+'.html"]');if(c){var b=c.querySelector("b");var sv=c.querySelector(".ic svg");links.push('<a href="'+c.getAttribute("href")+'">'+(sv?sv.outerHTML.replace("<svg",'<svg class="pi"'):"")+(b?b.innerHTML:sl)+'</a>')}});
if(!links.length)return;var n=document.createElement("nav");n.className="pop recent";n.innerHTML="<b>"+CK+(T[L]||T.ja)+"</b>"+links.join("");pop.parentNode.insertBefore(n,pop)});
})();

(function(){
var h=document.documentElement,L=(h.getAttribute("data-lang")||h.getAttribute("lang")||"ja").slice(0,2),nv=navigator;
try{if((nv.connection&&nv.connection.saveData)||(nv.deviceMemory&&nv.deviceMemory<=2)||(nv.hardwareConcurrency&&nv.hardwareConcurrency<=2))h.classList.add("lite")}catch(e){}
var S={
ja:["保存しました。次はこちらも便利です","ほかのツール","ファイルが大きめです（%sMB）","端末の中だけで処理するため、時間がかかったり止まったりすることがあります。分割するか、ページ数を減らしてからお試しください。","うまく処理できませんでした","ファイルが大きすぎるか、形式が対応していない可能性があります。小さく分割してもう一度お試しください。"],
en:["Saved. You may also need","More tools","This file is large (%s MB)","Everything runs inside your device, so it may be slow or stall. Try splitting the file or reducing the pages first.","Processing failed","The file may be too large or in an unsupported format. Split it into smaller parts and try again."],
zh:["已保存。接下来还可以","更多工具","文件较大（%s MB）","所有处理都在您的设备内完成，可能会较慢甚至卡住。建议先拆分文件或减少页数。","处理失败","文件可能过大或格式不受支持。请拆分成较小的文件后重试。"],
es:["Guardado. También puede servirte","Más herramientas","El archivo es grande (%s MB)","Todo se procesa en tu dispositivo, así que puede tardar o bloquearse. Prueba a dividir el archivo o reducir las páginas.","No se pudo procesar","El archivo puede ser demasiado grande o de un formato no compatible. Divídelo en partes más pequeñas e inténtalo de nuevo."],
ko:["저장했습니다. 다음 도구도 유용해요","다른 도구","파일이 큽니다(%sMB)","모든 처리가 기기 안에서만 이루어져 오래 걸리거나 멈출 수 있습니다. 파일을 나누거나 페이지 수를 줄여 보세요.","처리하지 못했습니다","파일이 너무 크거나 지원하지 않는 형식일 수 있습니다. 작게 나눠서 다시 시도해 주세요."],
pt:["Salvo. Também pode ser útil","Mais ferramentas","O arquivo é grande (%s MB)","Tudo é processado no seu dispositivo, então pode demorar ou travar. Tente dividir o arquivo ou reduzir as páginas.","Não foi possível processar","O arquivo pode ser grande demais ou de formato não compatível. Divida em partes menores e tente de novo."],
fr:["Enregistré. Vous aurez peut-être aussi besoin de","Plus d’outils","Le fichier est volumineux (%s Mo)","Tout est traité sur votre appareil : cela peut être lent ou se bloquer. Essayez de diviser le fichier ou de réduire les pages.","Échec du traitement","Le fichier est peut-être trop volumineux ou d’un format non pris en charge. Divisez-le et réessayez."],
it:["Salvato. Potrebbe servirti anche","Altri strumenti","Il file è grande (%s MB)","Tutto viene elaborato sul tuo dispositivo, quindi potrebbe essere lento o bloccarsi. Prova prima a dividere il file o a ridurre le pagine.","Elaborazione non riuscita","Il file potrebbe essere troppo grande o in un formato non supportato. Dividilo in parti più piccole e riprova."],
ru:["Сохранено. Вам также могут пригодиться","Другие инструменты","Файл большой (%s МБ)","Вся обработка идёт на вашем устройстве, поэтому она может быть медленной или зависнуть. Сначала попробуйте разделить файл или уменьшить число страниц.","Не удалось обработать","Файл может быть слишком большим или в неподдерживаемом формате. Разделите его на части поменьше и повторите попытку."],
vi:["Đã lưu. Có thể bạn cũng cần","Công cụ khác","Tệp khá lớn (%s MB)","Mọi thao tác chạy ngay trên thiết bị của bạn nên có thể chậm hoặc bị treo. Hãy thử tách tệp hoặc giảm số trang trước.","Xử lý không thành công","Tệp có thể quá lớn hoặc có định dạng không được hỗ trợ. Hãy tách thành các phần nhỏ hơn rồi thử lại."],
tr:["Kaydedildi. Şunlar da işinize yarayabilir","Diğer araçlar","Dosya büyük (%s MB)","Her şey cihazınızda çalıştığı için yavaşlayabilir veya takılabilir. Önce dosyayı bölmeyi veya sayfa sayısını azaltmayı deneyin.","İşlem başarısız oldu","Dosya çok büyük olabilir ya da biçimi desteklenmiyor olabilir. Daha küçük parçalara bölüp yeniden deneyin."],
de:["Gespeichert. Das könnte auch nützlich sein","Weitere Werkzeuge","Die Datei ist groß (%s MB)","Alles läuft auf Ihrem Gerät, daher kann es langsam werden oder hängen. Teilen Sie die Datei vorher auf oder reduzieren Sie die Seitenzahl.","Verarbeitung fehlgeschlagen","Die Datei ist möglicherweise zu groß oder hat ein nicht unterstütztes Format. Teilen Sie sie in kleinere Teile und versuchen Sie es erneut."],
hi:["सहेज लिया गया। ये भी काम आ सकते हैं","और टूल","फ़ाइल बड़ी है (%s MB)","सारा काम आपके डिवाइस पर ही होता है, इसलिए यह धीमा हो सकता है या अटक सकता है। पहले फ़ाइल को बाँट लें या पेज कम कर लें।","प्रोसेस नहीं हो सका","फ़ाइल बहुत बड़ी हो सकती है या उसका फ़ॉर्मैट समर्थित नहीं है। उसे छोटे हिस्सों में बाँटकर फिर कोशिश करें।"],
id:["Tersimpan. Mungkin Anda juga perlu","Alat lainnya","Berkas cukup besar (%s MB)","Semua diproses di perangkat Anda, jadi bisa lambat atau macet. Coba pisahkan berkas atau kurangi jumlah halaman.","Gagal memproses","Berkas mungkin terlalu besar atau formatnya tidak didukung. Pisahkan menjadi bagian lebih kecil lalu coba lagi."]
};var T=S[L]||S.ja,tm,picked=false,home=L==="ja"?"/":"/"+L+"/";
function box(){var b=document.getElementById("pm-toast");if(!b){b=document.createElement("div");b.id="pm-toast";b.setAttribute("role","status");b.setAttribute("aria-live","polite");document.body.appendChild(b)}return b}
function show(html,warn,ms){var b=box();b.className=warn?"warn":"";b.innerHTML=html+'<button class="x" type="button" aria-label="close">×</button>';b.querySelector(".x").onclick=function(){b.classList.remove("on")};void b.offsetWidth;b.classList.add("on");clearTimeout(tm);tm=setTimeout(function(){b.classList.remove("on")},ms||12000)}
function nm(a){var b=a.querySelector("b");if(!b)return a.textContent.trim();var s=b.querySelector('span[lang="'+L+'"]')||b;return s.textContent.trim()}
var shown=0;
document.addEventListener("click",function(e){var a=e.target.closest&&e.target.closest("a[download]");if(!a||Date.now()-shown<4000)return;shown=Date.now();
setTimeout(function(){var ls=[].slice.call(document.querySelectorAll("#next .ncards a.tool")).slice(0,3).map(function(x){return '<a href="'+x.getAttribute("href")+'">'+nm(x)+"</a>"});
ls.push('<a href="'+home+'">'+T[1]+"</a>");show("<b>✓ "+T[0]+"</b>"+'<div class="nx">'+ls.join("")+"</div>",false,14000)},500)},true);
document.addEventListener("change",function(e){var t=e.target;if(!t||t.type!=="file"||!t.files)return;picked=true;var sz=0;for(var i=0;i<t.files.length;i++)sz+=t.files[i].size;
if(sz>50*1048576)show("<b>"+T[2].replace("%s",Math.round(sz/1048576))+"</b>"+T[3],true,16000)},true);
window.addEventListener("unhandledrejection",function(e){if(!picked)return;var r=e.reason,m=r&&(r.message||String(r))||"";if(/PDFLib|pdfjsLib|is not defined|Failed to fetch|Load failed/i.test(m))return;show("<b>"+T[4]+"</b>"+T[5],true,14000)});
})();

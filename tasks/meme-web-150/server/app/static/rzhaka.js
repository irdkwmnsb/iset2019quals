let anime = document.getElementById('container'),
    slide = 0,
    mult = 10;

setInterval(function(){
    slide += mult;
    if(slide % 100 == 0){
        mult = -mult;
    }
    anime.style = 'filter: invert(' + slide + '%);';
}, 12);
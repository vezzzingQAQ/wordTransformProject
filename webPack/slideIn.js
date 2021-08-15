function getClientHeight(){
    var clientHeight=0;
    if(document.body.clientHeight&&document.documentElement.clientHeight){
        var clientHeight = (document.body.clientHeight<document.documentElement.clientHeight)?document.body.clientHeight:document.documentElement.clientHeight;
    }
    else{
        var clientHeight = (document.body.clientHeight>document.documentElement.clientHeight)?document.body.clientHeight:document.documentElement.clientHeight;
    }
    return clientHeight;
}

function scrollAnimate(){
    //blockText
    var animateBlock1=document.querySelectorAll(".slideIn");
    window.addEventListener("scroll",function(){
        //var value=window.scrollY;
        for(var i=0;i<animateBlock1.length;i++){
            console.log(animateBlock1[i].offsetTop)
            if(animateBlock1[i].offsetTop-document.documentElement.scrollTop<=getClientHeight()){
                animateBlock1[i].style.marginTop="2px";
            }else{
                animateBlock1[i].style.marginTop="200px";
            }
        }
    })
}

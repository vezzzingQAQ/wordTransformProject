function Vector(x,y){
    this.x=x;
    this.y=y;
    this.add=function(anotherVector){
        this.x+=anotherVector.x;
        this.y+=anotherVector.y;
    }
    this.mult=function(num){
        this.x*=num;
        this.y*=num;
    }
}
function Letter(x,y,vx,vy,r,id){
    this.position=new Vector(x,y);
    this.velocity=new Vector(vx,vy);
    this.radius=r;
    this.id=id;
    this.color=0;
    this.update=function(){
        this.position.add(this.velocity);
    }
    this.checkEdges=function(){
        if(this.position.x-this.radius<0 || this.position.x+this.radius>window.innerWidth){
            if(this.position.x-this.radius<0){
                this.position.x=this.radius;
            }else{
                this.position.x=window.innerWidth-this.radius;
            }
            this.velocity.x*=-1;
        }
        if(this.position.y-this.radius<0 || this.position.y+this.radius*2>window.innerHeight){
            if(this.position.y-this.radius<0){
                this.position.y=this.radius;
            }else{
                this.position.y=window.innerHeight-this.radius*2;
            }
            this.velocity.y*=-1;
        }
    }
    this.display=function(){
        var element=document.querySelector("#act"+this.id);
        //element.style.left=this.position.x+"px;";
        //element.style.top=this.position.y+"px;";
        element.style.cssText="left:"+this.position.x+"px;top:"+this.position.y+"px;color:rgb("+this.color+","+this.color+","+this.color+",200);";
    }
}
function slideTo(position,time){
    var currentScroll=window.scrollY;
    var speed=(position-currentScroll)/(50*time);
    console.log(currentScroll);
    var timer1=setInterval(function(){
        currentScroll+=speed;
        window.scrollTo(0,currentScroll);
        if((speed<0 && currentScroll<=position)||(speed>0 && currentScroll>=position)){
            clearInterval(timer1);
        }
    },20)
}


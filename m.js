function update () {
  
    v_date = new Date();
        if(  new String(v_date.getMonth()).length === 1) {
            document.getElementById("a1").innerHTML = 0;
            document.getElementById("a2").innerHTML = v_date.getMonth()+1;
            document.getElementById("a3").innerHTML = new String(v_date.getFullYear())[0];
            document.getElementById("a4").innerHTML = new String(v_date.getFullYear())[1];
            document.getElementById("a5").innerHTML = new String(v_date.getFullYear())[2];
            document.getElementById("a6").innerHTML = new String(v_date.getFullYear())[3];

            document.getElementById("a7").innerHTML = new String(v_date.getDate())[0];
            document.getElementById("a8").innerHTML = new String(v_date.getDate())[1];
            
            document.getElementById("a9").innerHTML = new String(v_date.getHours())[0];
            document.getElementById("aa").innerHTML = new String(v_date.getHours())[1]  ? "undefined": "0";
            document.getElementById("ab").innerHTML = new String(v_date.getMinutes())[0];
            document.getElementById("ac").innerHTML = new String(v_date.getMinutes())[1] ? "undefined": "0";
            document.getElementById("ad").innerHTML = new String(v_date.getSeconds())[0];
            document.getElementById("ae").innerHTML = new String(v_date.getSeconds())[1] ? "undefined": "0";

        } 
             
 


}
update();
setInterval(update,1000);

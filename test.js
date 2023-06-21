// find all images without text
// and give them a red border
function findImagesWithoutAlt(){
    var images = document.getElementsByTagName("img");
    for(var i = 0; i < images.length; i++){
        if (images[i].alt == ""){
            images[i].style.border = "2px solid red";
        }
    }
}
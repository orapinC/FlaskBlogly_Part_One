
//
// JS vanilla version
// file:app.js + index.html
// **problem with remove
//Uncaught (in promise) TypeError: Cannot read properties of undefined (reading 'images')
//at getImages (app.js:15.42)
//

function appendGif(res){
    //random select img
    const imgIndx = Math.floor(Math.random()*res.data.length);
    const imgSelected = res.data[imgIndx].images.original.url;
    //appendGif
    const GifSection = document.querySelector(".GIFs-section");
    const newGif = document.createElement('div');
    newGif.setAttribute('id','sub-gif');
    newGif.innerHTML = `<img src="${imgSelected}" height="200" alt="gif picture">`; 
    GifSection.append(newGif);
}

//get GIF when form submit based on the search term
const btn = document.querySelector('#search-form');
btn.addEventListener('submit', async function(e){
    e.preventDefault();
    const searchTerm = e.target.querySelector('#search-term').value;
    const imgs = await axios.get(`https://api.giphy.com/v1/gifs/search?q=${searchTerm}&api_key=T3ecO0EBnCrjnOoiOP5W7Y5kfnuH3lsZ`);
    //clear search form
    const form = document.querySelector('#search-form');
    form.reset();
    // appending GIFs
    appendGif(imgs.data);    
});

//remove GIFs
const remove = document.querySelector('#remove');
remove.addEventListener('click',function(e){
    const removeGif = document.querySelector(".GIFs-section");
    while(removeGif.firstChild){
        removeGif.removeChild(removeGif.firstChild);
    }
});
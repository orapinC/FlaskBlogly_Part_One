function randomGame(){
    let counter = 0;
    let timerId = setInterval(function(){ if(Math.random()>0.75){
                                              clearInterval(timerId);
                                              counter++;
                                              console.log('Number of tires:' + counter)
                                            } else {
                                              counter++;
                                            }
    },1000);
  }
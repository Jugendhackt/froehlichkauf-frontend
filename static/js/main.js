$(document).on('click','#download-button', function(event, test){

    var barcode = $("#barcode").val();
    console.log(barcode);

    console.log($(location).attr('href'));

    event.preventDefault();

    var url = $(location).attr('origin') + "/barcode/" + barcode;
    $(location).attr('href', url);

});

$(document).on('click','#back', function(event){
    event.preventDefault();
    $(location).attr('href', $(location).attr('origin'));
});



/*$(document).ready(function () {
    $('#download-button').on('click', function (e) {
        console.log("Test!")
        /*e.preventDefault();
        $('#download-button').css({'display': 'none'});
        $('#barcode-input').css({'display': 'block'});*/
//    });

 //   $("")

/*    Quagga.init({
    inputStream : {
      name : "Live",
      type : "LiveStream",
      target: document.querySelector('#yourElement')    // Or '#yourElement' (optional)
    },
    decoder : {
      readers : ["code_128_reader"]
    }
  }, function(err) {
      if (err) {
          console.log(err);
          return
      }
      console.log("Initialization finished. Ready to start");
      Quagga.start();
  });*/


//});*/
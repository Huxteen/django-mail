$(document).ready(function () {

    // To Initialise Date picker
    $("#datepicker-view-start").datepicker({
        autoClose: true,
        viewStart: 2
    });

    // To query the database for the search fields

 
  




  
    // To capitalize the first letter of any string
    function capitalize(s) { return s.toUpperCase(); }
    String.prototype.capitalize = function () {
        return this.toString().replace(/\b[a-z]/g, capitalize);
    };
    
});




$(document).ready(function(){
    $("button").click(function(){
        var a1 = parseInt($("#bil1").val());
        var a2 = parseInt($("#bil2").val());
        var a3 = parseInt($("#bil3").val());
        var a4 = parseInt($("#bil4").val());
        var a5 = parseInt($("#bil5").val());
        // hapus nilai p
        $("p").empty();
        // nilai Mean
        temp = (a1 + a2 + a3 + a4 + a5)/5;
        $("#hasil1").append(temp);
        // array nilai input
        var Array = [a1,a2,a3,a4,a5];
        // alert($.sum(Array));
        // nilai Max
        max = Math.max(...Array);
        $("#hasil2").append(max);
        // nilai Min
        min = Math.min(...Array);
        $("#hasil3").append(min);
        // nilai Modulus
        temp = {};
        var maks = Array[0], count = 1;
        for (var i = 0; i < Array.length; i++) {
            var ank = Array[i];
            if (temp[ank] == null) {
                temp[ank] = 1;
            } else {
                temp[ank]++;
            }
            if (temp[ank] > count) {
                maks = ank;
                count = temp[ank];
            }
        }
        if (count == 1) {
            $("#hasil4").append("Modus Tidak Ada");
        } else {
            $("#hasil4").append(maks);
        }
    });
});
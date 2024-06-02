"use strict";
document.write('<table border="1" width="300">');
for(let i = 1; i <= 10; i++){
    document.write("<tr align='center'>");
    for(let j = 1; j <= 10; j++){
        if((i + j) %2 == 0){
        document.write("<td bgcolor=red>" + j * i + "</td>")
        }
        else{
            document.write("<td bgcolor=yellow>" + j * i + "</td>");
        }
    }
    document.write("</tr>");
}
document.write("</table>");

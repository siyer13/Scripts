#!/bin/bash

eta=$1
echo $eta
today=`date +%m/%d/%Y`
yesterday=`date -d '-2 day'  '+%m/%d/%Y'`
recipients="siyer@gmail.com"
from="siyer@gmail.com"
subject="Delay mail($today)"
message="
<html>

<body>
    <table border='1' width='600px'>
        <thead>
            <th>  Data source refresh delayed.</th>
        </thead>
    </table>
    <table border='1' width='600px'>
        <tbody bgcolor='#FFFFCC'>
            <tr>
                <td> <b> Start Date: $today </td>
                <td> <b> Target group:  Analysts </td>
            </tr>
        </tbody>
    </table>
    <table border='1' width='600px'>
        <tbody>
            <tr>
                <td>
                    <h3><u>Summary:</u></h3> Refresh of tasks &amp; some other datasources are delayed
                    due to cluster, airflow and lock issues.
                    <br><br>
                    Our pipelines had to be restarted and are behind schedule. Hive tables and tableau datasoures will be available by <b>$eta</b> today. Data available is
                    complete as of <b>$yesterday</b>.
                    <br><br>
                    Apologies for any inconvinience caused, and feel free to reach out to us if you have any questions.
                    <br><br>
                    <h3><u>Contact:</u></h3>
                    <b>Email: </b> <a href test@gmail.com> esa-support </a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>IM: </b>
                    <a href> Yuhooo </a>
                </td>
            </tr>
        </tbody>
    </table>


</body>

</html>"

mail  -a 'MIME-Version: 1.0' -a 'Content-Type: text/html; charset=iso-8859-1' "$recipients" -s "$subject" << EOF
$message
EOF


#mail -a 'MIME-Version: 1.0' -a 'Content-Type: text/html; charset=iso-8859-1' siyer@gmail.com

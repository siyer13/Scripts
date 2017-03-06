#!/bin/bash

today=`date +%m/%d/%Y`
yesterday=`date -d "yesterday 13:00 " '+%m/%d/%Y'`
hours="1"
ETA="9"

recipients="siyer@pandora.com"
subject="Enterprise Analytics: Delay in PvA data refreshes ($today)"
message="<html>

<body>
    <table border='1' width='600px'>
        <thead>
            <th> <h4> PvA Data source refresh delays. </h4></th>
        </thead>
    </table>
    <table border='1' width='600px'>
        <tbody>
            <tr>
                <td> <b> Start today: $today </td>
                <td> <b> Target group: PvA Analysts </td>
            </tr>
        </tbody>
    </table>
    <table border='1' width='600px'>
        <tbody>
            <tr>
                <td>
                    <h3><u>Summary:</u></h3> Today- The refresh of the ESA Daily Ad Revenue Metrics nbsp; ESA Quarterly Ad Revenue Metrics datasources are delayed
                    due to airflow and lock issues.
                    <br><br>
                    Our pipelines had to be restarted and are behind schedule. Hive tables and tableau datasoures will be available by EOD today. Data available is
                    complete as of $yesterday
                    <br><br>
                    Apologies for any inconvinience caused, and feel free to reach out to us if you have any questions.
                    <br><br>
                    <h3><u>Contact:</u></h3>
                    <b>Email: </b> <a href mailto:dist-esa-support@pandora.com> esa-support </a> <b>Slack: </b> #es-analytics
                </td>
            </tr>
        </tbody>
    </table>


</body>

</html>"

mail  -a 'MIME-Version: 1.0' -a 'Content-Type: text/html; charset=iso-8859-1'  "$recipients" -s "$subject" << EOF
$message
EOF


#mail -a 'MIME-Version: 1.0' -a 'Content-Type: text/html; charset=iso-8859-1' siyer@pandora.com


var raw = {};
var cdata = [];

var init = function(){

    var f = "result_day-pos2.json";

    // example = {
    //     311: "Noise - Residential",
    //     NYPD: "ASSAULT 3 & RELATED OFFENSES",
    //     Zip_311: "10035",
    //     Zip_NYPD: "10451",
    //     startTime: "1262322000",
    //     endTime: "1451538000",
    //     relationship: 1
    // }


    const dlist = function (ds) {
        ret = [];
        i = 10;
        ds.forEach(function (d) {
            if (i == 0)
                return;
            dt = d.split('-');
            ret.push(new Date(parseInt(dt[0]), parseInt(dt[1]), parseInt(dt[2])));
            i -= 1;
        });
        return ret;
    };

    d3.json(f,
        function(data) {

            data.forEach(function (d) {
                if (d.ndays > 350) {
                    return;
                }
                k = {
                    complaint: d['311'],
                    crime: d.NYPD,
                    local: {complaint: d.Zip_311, crime: d.Zip_NYPD,},
                    date: dlist(d.days),
                    score: d.Relationship,
                };

                j = '';
                if (k.score == 1) {
                    j = d.Zip_311 + "-" + d.Zip_NYPD;
                } else {
                    j = d.Zip_NYPD + "-" + d.Zip_311;
                }

                if (!j in raw) (
                    raw[j] = []
                )

                k.name = j;
                raw[j] = k
            });

            cdata = Object.keys(raw).map(function (k) {
                return raw[k]['date'];
            })
        }
    );


            // var data = [
    //     { name: "http requests", data: [new Date('2014/09/15 13:24:54'), new Date('2014/09/15 13:25:03'), new Date('2014/09/15 13:25:05'), ] },
    //     { name: "SQL queries", data: [new Date('2014/09/15 13:24:57'), new Date('2014/09/15 13:25:04'), new Date('2014/09/15 13:25:04'),] },
    //     { name: "cache invalidations", data: [new Date('2014/09/15 13:25:12'),] }
    // ];

    var eventDropsChart = d3.chart.eventDrops();
    d3.select('#cloudline')
        .datum(cdata)
        .call(eventDropsChart);

};


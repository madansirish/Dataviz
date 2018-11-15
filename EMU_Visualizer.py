# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 19:24:40 2018

@author: DM00334783
"""



from sys import argv, exit
from os import getcwd, path
from datetime import datetime as dt, timedelta
from sqlite3 import connect
import json
import logging
import csv
import plotly
import plotly.graph_objs as go
from pandas import DataFrame, concat, read_csv, read_sql, read_sql_query
from PyQt5 import uic
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QInputDialog, QLineEdit, QMainWindow, QMessageBox


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
                    datefmt='%d-%b-%Y %H:%M:%S', filename='script/AirlineLogFile.log', filemode='w')
logger = logging.getLogger()


def gauge_function(obj):
    """ code for gauge"""
    logger.info('Entered into gauge function')
    size_object = QtWidgets.QDesktopWidget().screenGeometry(-1)
    width = size_object.width()
    size_object.height()
    try:
        bombardier_width = str(float((width-970)/2))+'px'
        curr = QtCore.QDir()
        image_name = curr.current().filePath('script/image/cockpit6.jpg')
        backward_image = curr.current().filePath("script/image/backward.png")
        forward_image = curr.current().filePath("script/image/forward.png")
        pause_image = curr.current().filePath("script/image/pause.png")
        stop_image = curr.current().filePath("script/image/stop.png")
        play_image = curr.current().filePath("script/image/play.png")
        gauge_minpath = curr.current().filePath("script/gauge.min.js")
        bootstrap_path = curr.current().filePath("script/bootstrap.min.css")
        eec1_qtot = json.dumps(obj['EEC1QTOT'])
        eec2_qtot = json.dumps(obj['EEC2QTOT'])
        eec1_nh = json.dumps(obj['EEC1NH'])
        eec2_nh = json.dumps(obj['EEC2NH'])
        eec1_npreq = json.dumps(obj['EEC1NPREQ'])
        eec2_npreq = json.dumps(obj['EEC2NPREQ'])
        eec1_itt = json.dumps(obj['EEC1ITT'])
        eec2_itt = json.dumps(obj['EEC2ITT'])
        eec1_mot = json.dumps(obj['EEC1MOT'])
        eec2_mot = json.dumps(obj['EEC2MOT'])
        eec1_mop = json.dumps(obj['EEC1MOP'])
        eec2_mop = json.dumps(obj['EEC2MOP'])
        eec1_pla = json.dumps(obj['EEC1PLA'])
        eec2_pla = json.dumps(obj['EEC2PLA'])
        pec1_cla = json.dumps(obj['PEC1CLA'])
        pec2_cla = json.dumps(obj['PEC2CLA'])
        eec1_nl = json.dumps(obj['EEC1NL'])
        eec2_nl = json.dumps(obj['EEC2NL'])
        emu1_wf = json.dumps(obj['EMU1WF'])
        emu2_wf = json.dumps(obj['EMU2WF'])
        meta_qtot = json.dumps(obj['meta_QTOT'])
        meta_nh = json.dumps(obj['meta_NH'])
        meta_npreq = json.dumps(obj['meta_NPREQ'])
        meta_itt = json.dumps(obj['meta_ITT'])
        meta_mot = json.dumps(obj['meta_MOT'])
        meta_mop = json.dumps(obj['meta_MOP'])
        meta_wf = json.dumps(obj['meta_WF'])
        meta_nl = json.dumps(obj['meta_NL'])
        time_min_max = json.dumps(obj['timeMinMax'])
        digital_clock = json.dumps(obj['Time'])
        boot_var = "css/bootstrap.min.css"
        font_var = "css/font-awesome.min.css"
        script_jvar = "script/jquery.min.js"
        script_bootvar = "script/bootstrap.min.js"
        script_gauge = "script/gauge.min.js"
        html = '''
       <html><head><meta charset="utf-8" />
    <title>Responsive Gauge</title>
    
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="bootstrappath">
    <script type="text/javascript" src="gaugeminpath"></script>

    <style>

        body {
            padding-top: 240px;
            margin-left: bombardierWidth;
            background-image: url("imagename");
            background-repeat: no-repeat;
            background-size: cover;
            width: 970px;
            }
        .fon{
            font-size: 12px;
            color:#fff;
            }   

        .fon_l{
            font-size: 12px;
            color:#fff;
            padding-left: 10px;
            
              }    

        .fon_r{
            font-size: 12px;
            color:#fff;
            padding-right: 10px;
              }   

        .box{
            width :100px;
            height:60px;
            }
            
        .backgroundclr{
            background:#000; //#71767c;
            border-radius: 8px;
                      }
                      
        .background{
            background: #000; //#71767c;
            border-radius: 4px;
                   }
        .column {
            float: left;
                }

        .left, .right {
          width: 27%;
                }

        .middle {
          width: 46%;
                }

        .row:after {
            content: "";
            display: table;
            clear: both;
                   }
                   
        .digitalreading{
            background-color: black;
            border:2px solid #ccc;
            border-radius: 4px;
            color: white;   
            text-align: center;
            text-decoration: none;
            font-size: 15px;
            font-family: timesnewroman;
            font-style: italic;
            width : 50px;
            height: 22px;
            margin-right: 8px;
            margin-left: 9px;
                       }

        .watch{
            background-color: #0f1620;
            border:9px solid #272e38;
            color: cyan;   
            text-align: center;
            text-decoration: none;
            font-size: 34px;
            text-shadow: 0 0 10px rgba(255, 255, 255, 1);
            width : 140px;
            height: 60px;
            margin: 10px;
            font-family: 'digital-7';
            position:relative;
            display:inline-block;
            }
             
         .watch1{
            background-color: #003366;
            border-radius: 3px;
            border:1px solid white;
            color: white;   
            width : 65px;
            height: 25px;
            position:relative;
            display:inline-block;
            }
.left_ps1L,.right_ps1R,.left_ps2L,.right_ps2R,.left_ps3L,.right_ps3R,.left_ps4L,.right_ps4R,.left_ps5L,.right_ps5R,.left_ps6L,.right_ps6R {
    position: relative;
}
.left_ps1L .glyphicon{
    position: absolute;
    top: -3%;
    right: 18.5%;
}

.right_ps1R .glyphicon{
    position: absolute;
    top: -3%;
    right: 71%;
}

.left_ps2L .glyphicon{
    position: absolute;
    top: -5%;
    right: 79%;
}

.right_ps2R .glyphicon{
    position: absolute;
    top: -5%;
    right: 16%;
}

.left_ps3L .glyphicon{
    position: absolute;
    top: 6.5%;
    right: 12%;
}

.right_ps3R .glyphicon{
    position: absolute;
    top: 6.5%;
    right: 42%;
}

.left_ps4L .glyphicon{
    position: absolute;
    top: 7%;
    right: 0%;
}

.right_ps4R .glyphicon{
    position: absolute;
    top: 7%;
    right: 30%;
}

.left_ps5L .glyphicon{
    position: absolute;
    top: 15%;
    right: 75%;
}

.right_ps5R .glyphicon{
    position: absolute;
    top: -16%;
    right: 9%;
}

.left_ps6L .glyphicon{
    position: absolute;
    top: 15%;
    right: 77%;
}

.right_ps6R .glyphicon{
    position: absolute;
    top: -16%;
    right: 8%;
}


    </style></head>

    <body>
    <div class="row">

    <div class="column left" style="margin-top:230px; padding-right:0px;">
        <td><canvas id="gauge-pla1"></canvas></td>
        <td><canvas id="gauge-pla2"></canvas></td>
    </div>

    <div class="column middle" >
    <div class="backgroundclr" style="padding-top:20px; padding-bottom: 8px;">
    
    <table border='0' width='65%' align="center"> 
        <!-- Row 1: Torque gauges  -->  
        <tr style="margin:0px;">      
            <td align='right' class="left_ps1L">
            <canvas id="gauge-ps1L"></canvas>
            <svg height="30" width="15" class="glyphicon">
            <line x1="10" y1="0" x2="10" y2="15" style="stroke:rgb(255,0,0);stroke-width:2" />
            </svg> 
            </td> 
            <td align='left' class="right_ps1R">
            <canvas id="gauge-ps1R"></canvas>
            <svg height="30" width="15" class="glyphicon">
            <line x1="10" y1="0" x2="10" y2="15" style="stroke:rgb(255,0,0);stroke-width:2" />
            </svg>
            </td>   
        </tr>

        <!-- Row 2: High pressure compressor Rotational Speed -->

        <tr> 
        <td align='center' colspan='2'> 
        <table border='0' width='100%'>
        <tr>
	<td align='Left' class="left_ps2L"> <canvas id="gauge-ps2L"></canvas> 
	<svg height="30" width="15" class="glyphicon">
        <line x1="10" y1="0" x2="10" y2="15" style="stroke:rgb(255,0,0);stroke-width:2" />
        </svg>
	</td> 
	<td align='right' class="right_ps2R"><canvas id="gauge-ps2R"></canvas>
	<svg height="30" width="15" class="glyphicon">
        <line x1="10" y1="0" x2="10" y2="15" style="stroke:rgb(255,0,0);stroke-width:2" />
        </svg>
	</td>
        </tr>
        </table>
        </td>
        </tr>

        <!-- Row 3: Propeller Speed -->
        <tr> 
        <td align='center' colspan='2'> 
        <table border='0' width='100%'>
        <tr>
            <td align='left'>
            <div> 
            <label class="fon_l">FF (Kg/H)</label>
            </div>
            <input class="digitalreading" type="button" value="0" id="ff_l" disabled>
            </td>
            <td align='right' class="left_ps3L"> <canvas id="gauge-ps3L"></canvas> 
            <svg height="30" width="12" class="glyphicon">
            <line x1="0" y1="10" x2="10" y2="0" style="stroke:rgb(255,0,0);stroke-width:2" />
            </svg>
            </td> 
            <td align='left' class="right_ps3R"><canvas id="gauge-ps3R"></canvas> 
            <svg height="30" width="12" class="glyphicon">
            <line x1="0" y1="10" x2="10" y2="0" style="stroke:rgb(255,0,0);stroke-width:2" />
            </svg>
            </td>
            <td align='right'>
            <div>
            <label class="fon_r">FF (Kg/H)</label>
            </div>
            <input class="digitalreading" type="button" value="0" id="ff_r" disabled>
            </td>
        </tr>
        </table>
        </td>
        </tr>

        <!-- Row 4: Indicated Turbine Temperature -->
        
        <tr> 
        <td align='center' colspan='2'> 
            <table border='0' width='100%'>
                <tr>
                <td align='left'>
                <div>
                <label class="fon_l">NL (%)</label>
                </div>
                <input class="digitalreading" type="button" value="0" id="nl_l" disabled>
                </td>
                
                <td align='right' class="left_ps4L"> <canvas id="gauge-ps4L"></canvas> 
                <!--<svg height="30" width="12" class="glyphicon">
                <line x1="0" y1="30" x2="100" y2="0" style="stroke:rgb(255,0,0);stroke-width:2" />
                </svg>-->
                </td> 
                <td align='Left' class="right_ps4R"><canvas id="gauge-ps4R"></canvas>
                <!--<svg height="30" width="12" class="glyphicon">
                <line x1="0" y1="30" x2="100" y2="0" style="stroke:rgb(255,0,0);stroke-width:2" />
                </svg>-->
                </td>
                
                <td align='right'>
                <div>
                <label class="fon_r">NL (%)</label>
                </div>
                <input class="digitalreading" type="button" value="0" id="nl_r" disabled>
                </td>
                </tr>
            </table>
        </td>
        </tr>

        <!-- Row 5: Oil Pressure and Oil Temperature -->
        <tr> 
        <td align='center' colspan='2'> 
        <table border='0' width='100%'>
        <tr>
        <td align='left' class="left_ps5L"><canvas id="gauge-ps5L"></canvas>
        <!--<svg height="30" width="10" class="glyphicon">
        <line x1="0" y1="0" x2="100" y2="30" style="stroke:rgb(255,0,0);stroke-width:2" />
        </svg>-->
        </td> 
        <td align='left' class="right_ps5R"><canvas id="gauge-ps5R"></canvas> 
        <!--<svg height="30" width="10" class="glyphicon">
        <line x1="0" y1="30" x2="100" y2="0" style="stroke:rgb(255,0,0);stroke-width:2" />
        </svg>-->
        </td> 
        <td  align='center' colspan='2'><input class="watch font-face" type="button" value=" "
             id="watch" disabled></td>

        <td align='right' class="left_ps6L"><canvas id="gauge-ps6L"></canvas> 
        <!--<svg height="30" width="10" class="glyphicon">
        <line x1="0" y1="0" x2="100" y2="30" style="stroke:rgb(255,0,0);stroke-width:2" />
        </svg>-->
        </td> 
        <td align='left' class="right_ps6R"><canvas id="gauge-ps6R"></canvas>
        <!--<svg height="30" width="10" class="glyphicon">
        <line x1="0" y1="30" x2="100" y2="0" style="stroke:rgb(255,0,0);stroke-width:2" />
        </svg>-->
        </td>  
        </tr>
        </table>
        </td>
        </tr>

        <tr> 
        <td align='center' colspan='2'> 
        <table border='0' width='100%'>
        <tr><p style="color: #fff">Time(Sec)</p></tr>
        </table>
        </td>
        </tr>
        
        </table>
    
    </div>
        <br>
        <div style="margin-top:-17px;" class="text-center background " >   
        <button onclick="backward()" id="back_bgcolor" title="Backward"><image src="backwardimage"/></button>
        <button onclick="pause()" id="pause_bgcolor" title="Pause"><image src="pauseimage"/></button>
        <button onclick="play()" id="play_bgcolor" title="Play"><image src="playimage"/></button>
        <button onclick="stop()" id="stop_bgcolor" title="Stop"><image src="stopimage"/></button> 
        <button onclick="forward()" id="forward_bgcolor" title="Forward"><image src="forwardimage"/></button>
        </div>
            
        <br>
        
        <div style="margin-top:-17px;" class="text-center background ">  
        <table>
        <tr>
        <td style="text-align: left; margin-top:1px;"><input class="watch1 font-face" type="button" value="" id="w1">
        </td>
        <td width="380px"><input id="seeker" type="range" value="0" width="10px" oninput="seeker()"/></td>
        <td style="margin-top:1px;"><input class="watch1 font-face" type="button" value="" id="w2"></td>
        </tr>
        </table>
        </div>
    
    </div>
    
    <div class="column left" style="margin-top:230px;">
    <td><canvas id="gauge-cla1"></canvas></td>
    <td><canvas id="gauge-cla2"></canvas></td>
    </div>
    
</div>

<div>&nbsp;</div>

<script>

////////////////////////////////Json data//////////////////////////////////

var metaTime =  timeMinMax;

var metaQTOT = meta_QTOT; 

var metaNH = meta_NH;

var metaNPREQ =meta_NPREQ;

var metaITT =meta_ITT;

var metaMOT = meta_MOT;

var metaMOP = meta_MOP;

//meta for PLA and CLA not available in excel sheet

var metaWF = meta_WF;

var metaNL = meta_NL;

var metaFuel_Kg = {
        MIN_VALUE: 0,
        MAX_VALUE: 9990};

var metaFuel_Degree = {
        MIN_VALUE: -99,
        MAX_VALUE: 99
    };

var metaSAT = {
        MIN_VALUE: -54,
        MAX_VALUE: 50
    };

/////////////////////////////////////////////////////////////////////////
    var watch_data = digitalClock;
   
    var data_QTOT1 = EEC1QTOT;
    
    var data_QTOT2 = EEC2QTOT;
    
    var data_NH1 = EEC1NH;
    
    var data_NH2 = EEC2NH;
    
    var data_NPREQ1= EEC1NPREQ;
    
    var data_NPREQ2 = EEC2NPREQ;
    
    var data_ITT1 =  EEC1ITT;
    
    var data_ITT2 = EEC2ITT;
    
    var data_MOT1 = EEC1MOT;
    
    var data_MOT2 = EEC2MOT;
    
    var data_MOP1= EEC1MOP;
    
    var data_MOP2 = EEC2MOP;

    var pla1 = EEC1PLA;

    var pla2 = EEC2PLA;

    var cla1 = PEC1CLA;

    var cla2 = PEC2CLA;

    var data_NL1 = EEC1NL;

    var data_NL2 = EEC2NL;
    
    var data_WF1 = EMU1WF;

    var data_WF2 = EMU2WF;

    var data_NTOP1 = 4580;

    var data_NTOP2 = 5071;
    
    //////////////////////////////////////////////////////////////////////////////////////////////////

    //PS1L Gauge
    var gaugePS1L = new RadialGauge({
        renderTo: 'gauge-ps1L',
        width: 110,
        height: 110,
        units: '%',
        title: 'QTOT',
        minValue: metaQTOT.MIN_VALUE,
        maxValue: metaQTOT.MAX_VALUE,
        majorTicks: [
           'metaQTOT.MIN_VALUE',
           'metaQTOT.MAX_VALUE'
        ],
        minorTicks: 1,
        ticksAngle: 270,
        startAngle: 45,colorTitle: "#fff",
        colorUnits: "#fff",
        strokeTicks: false,
        highlights  : [
             { from : metaQTOT.MIN_VALUE,  to : metaQTOT.THRESHOLD, color : 'green' },
             { from : metaQTOT.THRESHOLD,  to : metaQTOT.MAX_VALUE, color : '#fff' },
        ],
        highlightsWidth:5,
        valueInt: 1,
        valueDec: 0,
        colorPlate: "#000",
        colorMajorTicks: "#686868",
        colorMinorTicks: "#686868",
        colorTitle: "#fff",
        colorUnits: "#fff",
        colorNumbers: "#686868",
        valueBox: true,
        colorValueText: "#fff",
        colorValueBoxRect: "#fff",
        colorValueBoxRectEnd: "#fff",
        colorValueBoxBackground: "#000",
        colorValueBoxShadow: false,
        colorValueTextShadow: false,
        colorNeedleShadowUp: true,
        colorNeedleShadowDown: false,
        colorNeedle: "rgba(200, 50, 50, .75)",
        colorNeedleEnd: "rgba(200, 50, 50, .75)",
        colorNeedleCircleOuter: "rgba(200, 200, 200, 1)",
        colorNeedleCircleOuterEnd: "rgba(200, 200, 200, 1)",
        borderShadowWidth: 0,
        borders: false,
        borderInnerWidth: 0,
        borderMiddleWidth: 0,
        borderOuterWidth: 1,
        colorBorderOuter: "#000",
        colorBorderOuterEnd: "#fff",
        needleType: "arrow",
        needleWidth: 5,
        needleCircleSize: 9,
        needleCircleOuter: true,
        needleCircleInner: false,
        animationDuration: 100,
        animationRule: "bounce",
        fontNumbers: "Verdana",
        fontTitle: "Verdana",
        fontUnits: "Verdana",
        fontValue: "Led",
        fontValueStyle: 'italic',
        fontNumbersSize: 0,
        fontNumbersStyle: 'italic',
        fontNumbersWeight: 'bold',
        fontTitleSize: 45,
        fontUnitsSize: 45,
        fontValueSize: 60,
        animatedValue: true
    });
    gaugePS1L.draw();
    
    //PS1R Gauge
    var gaugePS1R = new RadialGauge({
        renderTo: 'gauge-ps1R',
        width: 110,
        height: 110,
        units: '%',
        title: 'QTOT',
        minValue: metaQTOT.MIN_VALUE,
        maxValue: metaQTOT.MAX_VALUE,
        majorTicks: [
           'metaQTOT.MIN_VALUE',
           'metaQTOT.MAX_VALUE'
        ],
        minorTicks: 1,
        ticksAngle: 270,
        startAngle: 45,
        strokeTicks: false,
         highlights  : [
             { from : metaQTOT.MIN_VALUE,  to : metaQTOT.THRESHOLD, color : 'green' },
             { from : metaQTOT.THRESHOLD,  to : metaQTOT.MAX_VALUE, color : '#fff' },
        ],
        highlightsWidth:5,
        valueInt: 1,
        valueDec: 0,
        colorPlate: "#000",
        colorMajorTicks: "#686868",
        colorMinorTicks: "#686868",
        colorTitle: "#fff",
        colorUnits: "#fff",
        colorNumbers: "#686868",
        valueBox: true,
        colorValueText: "#fff",
        colorValueBoxRect: "#fff",
        colorValueBoxRectEnd: "#fff",
        colorValueBoxBackground: "#000",
        colorValueBoxShadow: false,
        colorValueTextShadow: false,
        colorNeedleShadowUp: true,
        colorNeedleShadowDown: false,
        colorNeedle: "rgba(200, 50, 50, .75)",
        colorNeedleEnd: "rgba(200, 50, 50, .75)",
        colorNeedleCircleOuter: "rgba(200, 200, 200, 1)",
        colorNeedleCircleOuterEnd: "rgba(200, 200, 200, 1)",
        borderShadowWidth: 0,
        borders: false,
        borderInnerWidth: 0,
        borderMiddleWidth: 0,
        borderOuterWidth: 1,
        colorBorderOuter: "#000",
        colorBorderOuterEnd: "#fff",
        needleType: "arrow",
        needleWidth: 5,
        needleCircleSize: 9,
        needleCircleOuter: true,
        needleCircleInner: false,
        animationDuration: 100,
        animationRule: "dequint",
        fontNumbers: "Verdana",
        fontTitle: "Verdana",
        fontUnits: "Verdana",
        fontValue: "Led",
        fontValueStyle: 'italic',
        fontNumbersSize: 0,
        fontNumbersStyle: 'italic',
        fontNumbersWeight: 'bold',
        fontTitleSize: 45,
        fontUnitsSize: 45,
        fontValueSize: 60,
        animatedValue: true
    });
    gaugePS1R.draw();
    
    // PS2L Gauge 
    var gaugePS2L = new RadialGauge({
        renderTo: 'gauge-ps2L',
        width: 85,
        height: 85,
        units: '%',
        title: 'NH',
        minValue: metaNH.MIN_VALUE,
        maxValue: metaNH.MAX_VALUE,
        majorTicks: [
           'metaNH.MIN_VALUE',
           'metaNH.MAX_VALUE'
        ],        
        minorTicks: 1,
        ticksAngle: 270,
        startAngle: 45,
        strokeTicks: false,
        
         highlights  : [
             { from : metaNH.MIN_VALUE,  to : metaNH.THRESHOLD, color : '#fff' },
             { from : metaNH.THRESHOLD,  to : metaNH.THRESHOLD2, color : 'green' },
             { from : metaNH.THRESHOLD2,  to : metaNH.MAX_VALUE, color : '#fff' },  
        ],
        highlightsWidth:6,
        valueInt: 1,
        valueDec: 1,
        colorPlate: "#000",
        colorMajorTicks: "#686868",
        colorMinorTicks: "#686868",
        colorTitle: "#fff",
        colorUnits: "#fff",
        colorNumbers: "#686868",
        valueBox: true,
        colorValueText: "#fff",
        colorValueBoxRect: "#fff",
        colorValueBoxRectEnd: "#fff",
        colorValueBoxBackground: "#000",
        colorValueBoxShadow: false,
        colorValueTextShadow: false,
        colorNeedleShadowUp: true,
        colorNeedleShadowDown: false,
        colorNeedle: "rgba(200, 50, 50, .75)",
        colorNeedleEnd: "rgba(200, 50, 50, .75)",
        colorNeedleCircleOuter: "rgba(200, 200, 200, 1)",
        colorNeedleCircleOuterEnd: "rgba(200, 200, 200, 1)",
        borderShadowWidth: 0,
        borders: true,
        borderInnerWidth: 0,
        borderMiddleWidth: 0,
        borderOuterWidth: 0,
        colorBorderOuter: "#fafafa",
        colorBorderOuterEnd: "#cdcdcd",
        needleType: "arrow",
        needleWidth: 5,
        needleCircleSize: 9,
        needleCircleOuter: true,
        needleCircleInner: false,
        animationDuration: 100,
        animationRule: "dequint",
        fontNumbers: "Verdana",
        fontTitle: "Verdana",
        fontUnits: "Verdana",
        fontValue: "Led",
        fontValueStyle: 'italic',
        fontNumbersSize: 0,
        fontNumbersStyle: 'italic',
        fontNumbersWeight: 'bold',
        fontTitleSize: 65,
        fontUnitsSize: 65,
        fontValueSize: 75,
        animatedValue: true
    });
    gaugePS2L.draw();
    
    //PS2R Gauge
    var gaugePS2R = new RadialGauge({
        renderTo: 'gauge-ps2R',
        width: 85,
        height: 85,
        units: '%',
        title: 'NH',
        minValue: metaNH.MIN_VALUE,
        maxValue: metaNH.MAX_VALUE,
        majorTicks: [
           'metaNH.MIN_VALUE',
           'metaNH.MAX_VALUE'
        ],
        minorTicks: 1,
        ticksAngle: 270,
        startAngle: 45,
        strokeTicks: false,
         highlights  : [
             { from : metaNH.MIN_VALUE,  to : metaNH.THRESHOLD, color : '#fff' },
             { from : metaNH.THRESHOLD,  to : metaNH.THRESHOLD2, color : 'green' },
             { from : metaNH.THRESHOLD2,  to : metaNH.MAX_VALUE, color : '#fff' },
        ],
        highlightsWidth:6,
        valueInt: 1,
        valueDec: 1,
        colorPlate: "#000",
        colorMajorTicks: "#686868",
        colorMinorTicks: "#686868",
        colorTitle: "#fff",
        colorUnits: "#fff",
        colorNumbers: "#686868",
        valueBox: true,
        colorValueText: "#fff",
        colorValueBoxRect: "#fff",
        colorValueBoxRectEnd: "#fff",
        colorValueBoxBackground: "#000",
        colorValueBoxShadow: false,
        colorValueTextShadow: false,
        colorNeedleShadowUp: true,
        colorNeedleShadowDown: false,
        colorNeedle: "rgba(200, 50, 50, .75)",
        colorNeedleEnd: "rgba(200, 50, 50, .75)",
        colorNeedleCircleOuter: "rgba(200, 200, 200, 1)",
        colorNeedleCircleOuterEnd: "rgba(200, 200, 200, 1)",
        borderShadowWidth: 0,
        borders: true,
        borderInnerWidth: 0,
        borderMiddleWidth: 0,
        borderOuterWidth: 0,
        colorBorderOuter: "#fafafa",
        colorBorderOuterEnd: "#cdcdcd",
        needleType: "arrow",
        needleWidth: 5,
        needleCircleSize: 9,
        needleCircleOuter: true,
        needleCircleInner: false,
        animationDuration: 100,
        animationRule: "dequint",
        fontNumbers: "Verdana",
        fontTitle: "Verdana",
        fontUnits: "Verdana",
        fontValue: "Led",
        fontValueStyle: 'italic',
        fontNumbersSize: 0,
        fontNumbersStyle: 'italic',
        fontNumbersWeight: 'bold',
        fontTitleSize: 65,
        fontUnitsSize: 65,
        fontValueSize: 75,
        animatedValue: true
    });
    gaugePS2R.draw();
    
    //PS3L Gauge
    var gaugePS3L = new RadialGauge({
        renderTo: 'gauge-ps3L',
        width: 95,
        height: 95,
        units: 'RPM',
        title: 'NP',
        minValue: metaNPREQ.MIN_VALUE,
        maxValue: metaNPREQ.MAX_VALUE,
        majorTicks: [
           'metaNPREQ.MIN_VALUE',
           'metaNPREQ.MAX_VALUE'
        ],
        minorTicks: 1,
        ticksAngle: 270,
        startAngle: 45,
        strokeTicks: false,
        highlights  : [
             { from : metaNPREQ.MIN_VALUE,  to : metaNPREQ.THRESHOLD, color : '#fff' },
             { from : metaNPREQ.THRESHOLD,  to : metaNPREQ.THRESHOLD2, color : 'green' },
             { from : metaNPREQ.THRESHOLD2,  to : metaNPREQ.THRESHOLD3, color : '#fff' },
             { from : metaNPREQ.THRESHOLD3,  to : metaNPREQ.MAX_VALUE, color : 'green' },
             
        ],
        highlightsWidth:5,
        valueInt: 1,
        valueDec: 0,
        colorPlate: "#000",
        colorMajorTicks: "#686868",
        colorMinorTicks: "#686868",
        colorTitle: "#fff",
        colorUnits: "#fff",
        colorNumbers: "#686868",
        valueBox: true,
        colorValueText: "#fff",
        colorValueBoxRect: "#fff",
        colorValueBoxRectEnd: "#fff",
        colorValueBoxBackground: "#000",
        colorValueBoxShadow: false,
        colorValueTextShadow: false,
        colorNeedleShadowUp: true,
        colorNeedleShadowDown: false,
        colorNeedle: "rgba(200, 50, 50, .75)",
        colorNeedleEnd: "rgba(200, 50, 50, .75)",
        colorNeedleCircleOuter: "rgba(200, 200, 200, 1)",
        colorNeedleCircleOuterEnd: "rgba(200, 200, 200, 1)",
        borderShadowWidth: 0,
        borders: false,
        borderInnerWidth: 0,
        borderMiddleWidth: 0,
        borderOuterWidth: 1,
        colorBorderOuter: "#000",
        colorBorderOuterEnd: "#fff",
        needleType: "arrow",
        needleWidth: 5,
        needleCircleSize: 9,
        needleCircleOuter: true,
        needleCircleInner: false,
        animationDuration: 100,
        animationRule: "dequint",
        fontNumbers: "Verdana",
        fontTitle: "Verdana",
        fontUnits: "Verdana",
        fontValue: "Led",
        fontValueStyle: 'italic',
        fontNumbersSize: 0,
        fontNumbersStyle: 'italic',
        fontNumbersWeight: 'bold',
        fontTitleSize: 50,
        fontUnitsSize: 50,
        fontValueSize: 62,
       animatedValue: true
    });
    gaugePS3L.draw();
    
    //PS3R Gauge
    var gaugePS3R = new RadialGauge({
        renderTo: 'gauge-ps3R',
        width: 95,
        height: 95,
        units: 'RPM',
        title: 'NP',
        minValue: metaNPREQ.MIN_VALUE,
        maxValue: metaNPREQ.MAX_VALUE,
        majorTicks: [
           'metaNPREQ.MIN_VALUE',
           'metaNPREQ.MAX_VALUE'
        ],
        minorTicks: 1,
        ticksAngle: 270,
        startAngle: 45,
        strokeTicks: false,
         highlights  : [
             { from : metaNPREQ.MIN_VALUE,  to : metaNPREQ.THRESHOLD, color : '#fff' },
             { from : metaNPREQ.THRESHOLD,  to : metaNPREQ.THRESHOLD2, color : 'green' },
             { from : metaNPREQ.THRESHOLD2,  to : metaNPREQ.THRESHOLD3, color : '#fff' },
             { from : metaNPREQ.THRESHOLD3,  to : metaNPREQ.MAX_VALUE, color : 'green' },
             
        ],
        highlightsWidth:5,
        valueInt: 1,
        valueDec: 0,
        colorPlate: "#000",
        colorMajorTicks: "#686868",
        colorMinorTicks: "#686868",
        colorTitle: "#fff",
        colorUnits: "#fff",
        colorNumbers: "#686868",
        valueBox: true,
        colorValueText: "#fff",
        colorValueBoxRect: "#fff",
        colorValueBoxRectEnd: "#fff",
        colorValueBoxBackground: "#000",
        colorValueBoxShadow: false,
        colorValueTextShadow: false,
        colorNeedleShadowUp: true,
        colorNeedleShadowDown: false,
        colorNeedle: "rgba(200, 50, 50, .75)",
        colorNeedleEnd: "rgba(200, 50, 50, .75)",
        colorNeedleCircleOuter: "rgba(200, 200, 200, 1)",
        colorNeedleCircleOuterEnd: "rgba(200, 200, 200, 1)",
        borderShadowWidth: 0,
        borders: false,
        borderInnerWidth: 0,
        borderMiddleWidth: 0,
        borderOuterWidth: 1,
        colorBorderOuter: "#000",
        colorBorderOuterEnd: "#fff",
        needleType: "arrow",
        needleWidth: 5,
        needleCircleSize: 9,
        needleCircleOuter: true,
        needleCircleInner: false,
        animationDuration: 100,
        animationRule: "dequint",
        fontNumbers: "Verdana",
        fontTitle: "Verdana",
        fontUnits: "Verdana",
        fontValue: "Led",
        fontValueStyle: 'italic',
        fontNumbersSize: 0,
        fontNumbersStyle: 'italic',
        fontNumbersWeight: 'bold',
        fontTitleSize: 50,
        fontUnitsSize: 50,
        fontValueSize: 62,
        animatedValue: true
    });    
    gaugePS3R.draw();
    
    //PS4L Gauge
    var gaugePS4L = new RadialGauge({
        renderTo: 'gauge-ps4L',
        width: 95,
        height: 95,
        units: '\u00B0C',
        title: 'ITT',
        minValue: metaITT.MIN_VALUE,
        maxValue: metaITT.MAX_VALUE,
        majorTicks: [
           'metaITT.MIN_VALUE',
           'metaITT.MAX_VALUE'
        ],
        minorTicks: 1,
        ticksAngle: 270,
        startAngle: 45,
        strokeTicks: false,
         highlights  : [
             { from : metaITT.MIN_VALUE,  to : metaITT.THRESHOLD, color : '#fff' },
             { from : metaITT.THRESHOLD,  to : metaITT.THRESHOLD2, color : 'green' },
             { from : metaITT.THRESHOLD2,  to : metaITT.MAX_VALUE, color : 'red' },
        ],
         highlightsWidth:5,
        valueInt: 1,
        valueDec: 0,
        colorPlate: "#000",
        colorMajorTicks: "#686868",
        colorMinorTicks: "#686868",
        colorTitle: "#fff",
        colorUnits: "#fff",
        colorNumbers: "#686868",
        valueBox: true,
        colorValueText: "#fff",
        colorValueBoxRect: "#fff",
        colorValueBoxRectEnd: "#fff",
        colorValueBoxBackground: "#000",
        colorValueBoxShadow: false,
        colorValueTextShadow: false,
        colorNeedleShadowUp: true,
        colorNeedleShadowDown: false,
        colorNeedle: "rgba(200, 50, 50, .75)",
        colorNeedleEnd: "rgba(200, 50, 50, .75)",
        colorNeedleCircleOuter: "rgba(200, 200, 200, 1)",
        colorNeedleCircleOuterEnd: "rgba(200, 200, 200, 1)",
        borderShadowWidth: 0,
        borders: false,
        borderInnerWidth: 0,
        borderMiddleWidth: 0,
        borderOuterWidth: 1,
        colorBorderOuter: "#000",
        colorBorderOuterEnd: "#fff",
        needleType: "arrow",
        needleWidth: 5,
        needleCircleSize: 9,
        needleCircleOuter: true,
        needleCircleInner: false,
        animationDuration: 100,
        animationRule: "dequint",
        fontNumbers: "Verdana",
        fontTitle: "Verdana",
        fontUnits: "Verdana",
        fontValue: "Led",
        fontValueStyle: 'italic',
        fontNumbersSize: 0,
        fontNumbersStyle: 'italic',
        fontNumbersWeight: 'bold',
        fontTitleSize: 50,
        fontUnitsSize: 50,
        fontValueSize: 62,
        animatedValue: true
    });
    gaugePS4L.draw();
    
    //PS4R Gauge
    var gaugePS4R = new RadialGauge({
        renderTo: 'gauge-ps4R',
        width: 95,
        height: 95,
        units: '\u00B0C',
        title: 'ITT',
        minValue: metaITT.MIN_VALUE,
        maxValue: metaITT.MAX_VALUE,
        majorTicks: [
           'metaITT.MIN_VALUE',
           'metaITT.MAX_VALUE'
        ],
        minorTicks: 1,
        ticksAngle: 270,
        startAngle: 45,
        strokeTicks: false,
         highlights  : [
             { from : metaITT.MIN_VALUE,  to : metaITT.THRESHOLD, color : '#fff' },
             { from : metaITT.THRESHOLD,  to : metaITT.THRESHOLD2, color : 'green' },
             { from : metaITT.THRESHOLD2,  to : metaITT.MAX_VALUE, color : 'red' },
        ],
        highlightsWidth:5,
        valueInt: 1,
        valueDec: 0,
        colorPlate: "#000",
        colorMajorTicks: "#686868",
        colorMinorTicks: "#686868",
        colorTitle: "#fff",
        colorUnits: "#fff",
        colorNumbers: "#686868",
        valueBox: true,
        colorValueText: "#fff",
        colorValueBoxRect: "#fff",
        colorValueBoxRectEnd: "#fff",
        colorValueBoxBackground: "#000",
        colorValueBoxShadow: false,
        colorValueTextShadow: false,
        colorNeedleShadowUp: true,
        colorNeedleShadowDown: false,
        colorNeedle: "rgba(200, 50, 50, .75)",
        colorNeedleEnd: "rgba(200, 50, 50, .75)",
        colorNeedleCircleOuter: "rgba(200, 200, 200, 1)",
        colorNeedleCircleOuterEnd: "rgba(200, 200, 200, 1)",
        borderShadowWidth: 0,
        borders: false,
        borderInnerWidth: 0,
        borderMiddleWidth: 0,
        borderOuterWidth: 1,
        colorBorderOuter: "#000",
        colorBorderOuterEnd: "#fff",
        needleType: "arrow",
        needleWidth: 5,
        needleCircleSize: 9,
        needleCircleOuter: true,
        needleCircleInner: false,
        animationDuration: 100,
        animationRule: "dequint",
        fontNumbers: "Verdana",
        fontTitle: "Verdana",
        fontUnits: "Verdana",
        fontValue: "Led",
        fontValueStyle: 'italic',
        fontNumbersSize: 0,
        fontNumbersStyle: 'italic',
        fontNumbersWeight: 'bold',
        fontTitleSize: 50,
        fontUnitsSize: 50,
        fontValueSize: 62,
        animatedValue: true
    });
   gaugePS4R.draw();
    
    //PS5L Gauge
    var gaugePS5L = new RadialGauge({
        renderTo: 'gauge-ps5L',
        width: 75,
        height: 75,
        units: '\u00B0C',
        title: 'MOT',
        minValue: metaMOT.MIN_VALUE,
        maxValue: metaMOT.MAX_VALUE,
        majorTicks: [
           'metaMOT.MIN_VALUE',
           'metaMOT.MAX_VALUE'
        ],     
        minorTicks: 1,
        ticksAngle: 180,
        startAngle: 0,
        strokeTicks: false,
        highlights  : [
             { from : metaMOT.MIN_VALUE,  to : metaMOT.THRESHOLD, color : 'green' },
             { from : metaMOT.THRESHOLD,  to : metaMOT.MAX_VALUE, color : '#fff' },
        ],
        highlightsWidth:7,
        valueInt: 1,
        valueDec: 0,
        colorPlate: "#000",
        colorMajorTicks: "#686868",
        colorMinorTicks: "#686868",
        colorTitle: "#fff",
        colorUnits: "#fff",
        colorNumbers: "#686868",
        valueBox: true,
        colorValueText: "#fff",
        colorValueBoxRect: "#fff",
        colorValueBoxRectEnd: "#fff",
        colorValueBoxBackground: "#000",
        colorValueBoxShadow: false,
        colorValueTextShadow: false,
        colorNeedleShadowUp: true,
        colorNeedleShadowDown: false,
        colorNeedle: "rgba(200, 50, 50, .75)",
        colorNeedleEnd: "rgba(200, 50, 50, .75)",
        colorNeedleCircleOuter: "rgba(200, 200, 200, 1)",
        colorNeedleCircleOuterEnd: "rgba(200, 200, 200, 1)",
        borderShadowWidth: 0,
        borders: false,
        borderInnerWidth: 0,
        borderMiddleWidth: 0,
        borderOuterWidth: 5,
        colorBorderOuter: "#fafafa",
        colorBorderOuterEnd: "#cdcdcd",
        needleType: "arrow",
        needleWidth: 5,
        needleCircleSize: 9,
        needleCircleOuter: true,
        needleCircleInner: false,
        animationDuration: 100,
        animationRule: "dequint",
        fontNumbers: "Verdana",
        fontTitle: "Verdana",
        fontUnits: "Verdana",
        fontValue: "Led",
        fontValueStyle: 'italic',
        fontNumbersSize: 0,
        fontNumbersStyle: 'italic',
        fontNumbersWeight: 'bold',
        fontTitleSize: 50,
        fontUnitsSize: 65,
        fontValueSize: 65,
        animatedValue: true
    });
    gaugePS5L.draw();
    
    //PS5R Gauge
    var gaugePS5R = new RadialGauge({
        renderTo: 'gauge-ps5R',
        width: 75,
        height: 75,
        units: 'PSI',
        title: 'MOP',
        minValue: metaMOP.MIN_VALUE,
        maxValue: metaMOP.MAX_VALUE,
        majorTicks: [
           'metaMOP.MIN_VALUE',
           'metaMOP.MAX_VALUE'
        ],      
        minorTicks: 1,
        ticksAngle: 180,
        startAngle: 180,
        strokeTicks: false,
        highlights  : [
             { from : metaMOP.MIN_VALUE,  to : metaMOP.THRESHOLD, color : 'yellow' },
             { from : metaMOP.THRESHOLD,  to : metaMOP.THRESHOLD2, color : 'green' },
             { from : metaMOP.THRESHOLD2,  to : metaMOP.MAX_VALUE, color : '#fff' },  
        ],
        highlightsWidth:7,
        valueInt: 1,
        valueDec: 0,
        colorPlate: "#000",
        colorMajorTicks: "#686868",
        colorMinorTicks: "#686868",
        colorTitle: "#fff",
        colorUnits: "#fff",
        colorNumbers: "#686868",
        valueBox: true,
        colorValueText: "#fff",
        colorValueBoxRect: "#fff",
        colorValueBoxRectEnd: "#fff",
        colorValueBoxBackground: "#000",
        colorValueBoxShadow: false,
        colorValueTextShadow: false,
        colorNeedleShadowUp: true,
        colorNeedleShadowDown: false,
        colorNeedle: "rgba(200, 50, 50, .75)",
        colorNeedleEnd: "rgba(200, 50, 50, .75)",
        colorNeedleCircleOuter: "rgba(200, 200, 200, 1)",
        colorNeedleCircleOuterEnd: "rgba(200, 200, 200, 1)",
        borderShadowWidth: 0,
        borders: false,
        borderInnerWidth: 0,
        borderMiddleWidth: 0,
        borderOuterWidth: 5,
        colorBorderOuter: "#fafafa",
        colorBorderOuterEnd: "#cdcdcd",
        needleType: "arrow",
        needleWidth: 5,
        needleCircleSize: 9,
        needleCircleOuter: true,
        needleCircleInner: false,
        animationDuration: 100,
        animationRule: "dequint",
        fontNumbers: "Verdana",
        fontTitle: "Verdana",
        fontUnits: "Verdana",
        fontValue: "Led",
        fontValueStyle: 'italic',
        fontNumbersSize: 0,
        fontNumbersStyle: 'italic',
        fontNumbersWeight: 'bold',
        fontTitleSize: 50,
        fontUnitsSize: 65,
        fontValueSize: 65,
        animatedValue: true 
    
    });
    gaugePS5R.draw();
    
    //PS6L Gauge
    var gaugePS6L = new RadialGauge({
        renderTo: 'gauge-ps6L',
       width: 75,
        height: 75,
        units: '\u00B0C',
        title: 'MOT',
        minValue: metaMOT.MIN_VALUE,
        maxValue: metaMOT.MAX_VALUE,
       majorTicks: [
           'metaMOT.MIN_VALUE',
           'metaMOT.MAX_VALUE'
        ], 
        minorTicks: 1,
        ticksAngle: 180,
        startAngle: 0,
        strokeTicks: false,
        highlights  : [
            { from : metaMOT.MIN_VALUE,  to : metaMOT.THRESHOLD, color : 'green' },
             { from : metaMOT.THRESHOLD,  to : metaMOT.MAX_VALUE, color : '#fff' }
             //{ from : 2650, to : 4000, color : 'rgba(225, 0, 0, 30)' }
        ],
        highlightsWidth:7,
        valueInt: 1,
        valueDec: 0,
        colorPlate: "#000",
        colorMajorTicks: "#686868",
        colorMinorTicks: "#686868",
        colorTitle: "#fff",
        colorUnits: "#fff",
        colorNumbers: "#686868",
        valueBox: true,
        colorValueText: "#fff",
        colorValueBoxRect: "#fff",
        colorValueBoxRectEnd: "#fff",
        colorValueBoxBackground: "#000",
        colorValueBoxShadow: false,
        colorValueTextShadow: false,
        colorNeedleShadowUp: true,
        colorNeedleShadowDown: false,
        colorNeedle: "rgba(200, 50, 50, .75)",
        colorNeedleEnd: "rgba(200, 50, 50, .75)",
        colorNeedleCircleOuter: "rgba(200, 200, 200, 1)",
        colorNeedleCircleOuterEnd: "rgba(200, 200, 200, 1)",
        borderShadowWidth: 0,
        borders: false,
        borderInnerWidth: 0,
        borderMiddleWidth: 0,
        borderOuterWidth: 5,
        colorBorderOuter: "#fafafa",
        colorBorderOuterEnd: "#cdcdcd",
        needleType: "arrow",
        needleWidth: 5,
        needleCircleSize: 9,
        needleCircleOuter: true,
        needleCircleInner: false,
        animationDuration: 100,
        animationRule: "dequint",
        fontNumbers: "Verdana",
        fontTitle: "Verdana",
        fontUnits: "Verdana",
        fontValue: "Led",
        fontValueStyle: 'italic',
        fontNumbersSize: 0,
        fontNumbersStyle: 'italic',
        fontNumbersWeight: 'bold',
        fontTitleSize: 50,
        fontUnitsSize: 65,
        fontValueSize: 65,
        animatedValue: true       
    
    });
    gaugePS6L.draw();
    
    //PS6R Gauge
    var gaugePS6R = new RadialGauge({
        renderTo: 'gauge-ps6R',
        plate: '#fff',
        width: 75,
        height: 75,
        units: 'PSI',
        title: 'MOP',
        minValue: metaMOP.MIN_VALUE,
        maxValue: metaMOP.MAX_VALUE,
        majorTicks: [
           'metaMOP.MIN_VALUE',
           'metaMOP.MAX_VALUE'
        ], 
        minorTicks: 1,
        ticksAngle: 180,
        startAngle: 180,
        strokeTicks: false,
        highlights  : [
             { from : metaMOP.MIN_VALUE,  to : metaMOP.THRESHOLD, color : 'yellow' },
             { from : metaMOP.THRESHOLD,  to : metaMOP.THRESHOLD2, color : 'green' },
             { from : metaMOP.THRESHOLD2,  to : metaMOP.MAX_VALUE, color : '#fff' },  
        ],
        highlightsWidth:7,
        circleShape: "half-left",
        valueInt: 1,
        valueDec: 0,
        colorPlate: "#000",
        colorMajorTicks: "#686868",
        colorMinorTicks: "#686868",
        colorTitle: "#fff",
        colorUnits: "#fff",
        colorNumbers: "#686868",
        valueBox: true,
        colorValueText: "#fff",
        colorValueBoxRect: "#fff",
        colorValueBoxRectEnd: "#fff",
        colorValueBoxBackground: "#000",
        colorValueBoxShadow: false,
        colorValueTextShadow: false,
        colorNeedleShadowUp: true,
        colorNeedleShadowDown: false,
        colorNeedle: "rgba(200, 50, 50, .75)",
        colorNeedleEnd: "rgba(200, 50, 50, .75)",
        colorNeedleCircleOuter: "rgba(200, 200, 200, 1)",
        colorNeedleCircleOuterEnd: "rgba(200, 200, 200, 1)",
        borderShadowWidth: 0,
        borders: false,
        borderInnerWidth: 0,
        borderMiddleWidth: 0,
        borderOuterWidth: 5,
        colorBorderOuter: "#fafafa",
        colorBorderOuterEnd: "#cdcdcd",
        needleType: "arrow",
        needleWidth: 5,
        needleCircleSize: 9,
        needleCircleOuter: true,
        needleCircleInner: false,
        animationDuration: 100,
        animationRule: "dequint",
        fontNumbers: "Verdana",
        fontTitle: "Verdana",
        fontUnits: "Verdana",
        fontValue: "Led",
        fontValueStyle: 'italic',
        fontNumbersSize: 0,
        fontNumbersStyle: 'italic',
        fontNumbersWeight: 'bold',
        fontTitleSize: 50,
        fontUnitsSize: 65,
        fontValueSize: 65,
        animatedValue: true 
    
    });
    gaugePS6R.draw();
    
    //CLA-left 
   var gaugeCLA1 = new LinearGauge({
        renderTo: 'gauge-cla1',
        width: 130,
        height: 330,
        units: "CLA-1",
        minValue: 0,
        maxValue: 100,
        majorTicks: [      
        "Fuel Off",
         "",
         "",
         "",
         "",
         "",
         "Feather)",
         "(Start / ",
         "",
         "",
         "",
         "Min",
         "",
         "",
         "",
         "Climb",
          "",
         "",
         "",
         "Max",
         ""
        ],
        minorTicks: 0,
        strokeTicks: true,
        highlights: [
            {
                "from": 85,
                "to": 100,
                "color": "rgba(200, 50, 50, .75)"
            }
        ],
        colorPlate: "#fff",
        colorNumbers:"#000",
        fontNumbersSize:23,
        fontNumbersStyle:"bold",
        borderShadowWidth: 1,
        borders: true,
        needleType: "arrow",
        needleWidth: 5,
        colorNeedle:"#ff0000",
        colorNeedleEnd: "#ff0000",
        animationDuration: 100,
        animationRule: "linear",
        //tickSide: "right",
        //numberSide: "right",
        //needleSide: "right",
        //barStrokeWidth: 10,
        tickSide: "left",
        numberSide: "right",
        needleSide: "left",
        barWidth:25,
        barStrokeWidth: 10,
        ticksPadding:-3,
        barBeginCircle: false,
        animatedValue: true,
        fontValueSize: 29,
        fontUnitsSize: 31,
        fontValueStyle:"bold",
        fontUnitsStyle:"bold",
        colorUnits:"#000"
    
    }); 
    gaugeCLA1.draw();
    
    //CLA-right
    var gaugeCLA2 = new LinearGauge({
        renderTo: 'gauge-cla2',
        width: 130,
        height: 330,
        units: "CLA-2",
        minValue: 0,
        maxValue: 100,
        majorTicks: [      
        "Fuel Off",
         "",
         "",
         "",
         "",
         "",
         "Feather)",
         "(Start / ",
         "",
         "",
         "",
         "Min",
         "",
         "",
         "",
         "Climb",
          "",
         "",
         "",
         "Max",
         ""
        ],
        minorTicks: 0,
        strokeTicks: true,
        highlights: [
            {
                "from": 85,
                "to": 100,
                "color": "rgba(200, 50, 50, .75)"
            }
        ],
        colorPlate: "#fff",
        colorNumbers:"#000",
        fontNumbersSize:23,
        fontNumbersStyle:"bold",
        borderShadowWidth: 1,
        borders: true,
        needleType: "arrow",
        needleWidth: 5,
        colorNeedle:"#ff0000",
        colorNeedleEnd: "#ff0000",
        animationDuration: 100,
        animationRule: "linear",
        //tickSide: "right",
        //numberSide: "right",
        //needleSide: "right",
        //barStrokeWidth: 10,
        tickSide: "left",
        numberSide: "right",
        needleSide: "left",
        barWidth:25,
        barStrokeWidth: 10,
        ticksPadding:-3,
        barBeginCircle: false,
        animatedValue: true,
        fontValueSize: 29,
        fontUnitsSize: 31,
        fontValueStyle:"bold",
        fontUnitsStyle:"bold",
        colorUnits:"#000"
    });
    gaugeCLA2.draw();
    
    //PLA-left
    var gaugePLA1 = new LinearGauge({
        renderTo: 'gauge-pla1',
        width: 132,
        height: 330,
        units: "PLA-1",
        minValue: 0,
        maxValue: 100,
        majorTicks: [
        "Max Rev",
         "",
         "",
         "",
         "Disc",
         "",
         "",
         "Idle",
         "Flight",
         "",
         "",
         "",
         "",
         "",
         "",
         "",
         "Rating",
         "",
         "",
         "",
         ""
        ],
        minorTicks: 10,
        strokeTicks: true,
        highlights: [
            {
                "from": 85,
                "to": 100,
                "color": "rgba(200, 50, 50, .75)"
            }
        ],
        colorPlate: "#fff",
        colorNumbers:"#000",
        fontNumbersSize:22,
        fontNumbersStyle:"bold",
        borderShadowWidth: 1,
        borders: true,
        needleType: "arrow",
        needleWidth: 5,
        colorNeedle:"#ff0000",
        colorNeedleEnd: "#ff0000",
        animationDuration: 100,
        animationRule: "linear",
        tickSide: "right",
        numberSide: "left",
        needleSide: "right",
        barWidth:25,
        barStrokeWidth: 10,
        ticksPadding:-4,
        barBeginCircle: false,
        animatedValue: true,
        fontValueSize: 29,
        fontUnitsSize: 31,
        fontValueStyle:"bold",
        fontUnitsStyle:"bold",
        colorUnits:"#000"
    });
    gaugePLA1.draw();
    
    //PLA2-right
    var gaugePLA2 = new LinearGauge({
        renderTo: 'gauge-pla2',
        width: 132,
        height: 330,
        units: "PLA-2",
        minValue: 0,
        maxValue: 100,
        majorTicks: [
        "Max Rev",
         "",
         "",
         "",
         "Disc",
         "",
         "",
         "Idle",
         "Flight",
         "",
         "",
         "",
         "",
         "",
         "",
         "",
         "Rating",
         "",
         "",
         "",
         ""
        ],
        minorTicks: 10,
        strokeTicks: true,
        highlights: [
            {
                "from": 85,
                "to": 100,
                "color": "rgba(200, 50, 50, .75)"
            }
        ],
        colorPlate: "#fff",
        colorNumbers:"#000",
        fontNumbersSize:22,
        fontNumbersStyle:"bold",
        borderShadowWidth: 1,
        borders: true,
        needleType: "arrow",
        needleWidth: 5,
        colorNeedle:"#ff0000",
        colorNeedleEnd: "#ff0000",
        animationDuration: 100,
        animationRule: "linear",
        tickSide: "right",
        numberSide: "left",
        needleSide: "right",
        barWidth:25,
        barStrokeWidth: 10,
        ticksPadding:-4,
        barBeginCircle: false,
        animatedValue: true,
        fontValueSize: 29,
        fontUnitsSize: 31,
        fontValueStyle:"bold",
        fontUnitsStyle:"bold",
        colorUnits:"#000"
    }); 
    gaugePLA2.draw();

///////////////////////////////////////////////////////////////////

////////////////////////////////////////////////Global variables//////////////////////////////////////////

 var tempX = 0;
 let myGuageInterval = 0;
  var button_bgcolor = "rgb(42, 109, 210)";//it should be in RGB format

////////////////////////////////////////////////Standard Watch//////////////////////////////////////////
    var big_watch =  document.getElementById('watch');
    big_watch.value=metaTime.minTime;
    document.getElementById('w1').value=metaTime.minTime;
    document.getElementById('w2').value=metaTime.maxTime;


    seekertempX = document.getElementById('seeker');
    var seeker_length = watch_data.length;
    document.getElementById('seeker').max=seeker_length-1;
    document.getElementById('seeker').min=0;

////////////////////////////////////////////////Move Seeker//////////////////////////////////////////
     if(true){
      seekertempX.addEventListener("input", 
             function(){
                         killIntervals();
                         getControlValues();
                       });

      }
     if(true){
      seekertempX.addEventListener("mouseup", 
             function(){
           //var play_btn = document.getElementById("play_bgcolor").style.backgroundColor;
           var stop_btn = document.getElementById("stop_bgcolor").style.backgroundColor;
           var pause_btn = document.getElementById("pause_bgcolor").style.backgroundColor;
           play();
           if(stop_btn == button_bgcolor){pause();}
           if(pause_btn == button_bgcolor){pause();}
  
        });
}
////////////////////////////////////////////////Seeker//////////////////////////////////////////

function seeker(){
           seekertempX = document.getElementById('seeker');
            var x = seekertempX.value
            gaugePS1L.value = data_QTOT1[x];
            gaugePS1R.value = data_QTOT2[x];

            gaugePS2L.value = data_NH1[x];
            gaugePS2R.value = data_NH2[x];

            gaugePS3L.value = data_NPREQ1[x];
            gaugePS3R.value = data_NPREQ2[x];

            gaugePS4L.value = data_ITT1[x];
            gaugePS4R.value = data_ITT2[x];

            gaugePS5L.value = data_MOT1[x];
            gaugePS5R.value = data_MOP1[x];

            gaugePS6L.value = data_MOT2[x];
            gaugePS6R.value = data_MOP2[x];

            big_watch.value=watch_data[x];

            gaugeCLA1.value = cla1[x];
            gaugeCLA2.value = cla2[x];
            gaugePLA1.value = pla1[x];
            gaugePLA2.value = pla2[x];

            document.getElementById('ff_l').value = data_WF1[x];
            document.getElementById('ff_r').value = data_WF2[x];
            document.getElementById('nl_l').value = data_NL1[x];
            document.getElementById('nl_r').value = data_NL2[x];
            }



////////////////////////////////////////////////Play//////////////////////////////////////////

function play(){
             debugger;
             //for button background
             document.getElementById("play_bgcolor").style.backgroundColor=button_bgcolor;
             document.getElementById("pause_bgcolor").style.backgroundColor="#fff";
             document.getElementById("stop_bgcolor").style.backgroundColor="#fff";
             document.getElementById("back_bgcolor").style.backgroundColor="#fff";
             document.getElementById("forward_bgcolor").style.backgroundColor="#fff";
          
             //First kill existing timers
             killIntervals();
            
             getControlValues();

             console.log('Play: tempX', tempX);
          //loop for gauges
             let start = Date.now();
             x = tempX;
   
                    var to = 500 * x;

                    myGuageInterval = setInterval(() => {
                        if (x >= watch_data.length) {
                            clearInterval(myGuageInterval);
                            console.log('Play: end of guage loop');
                            return;
                        }
        
                        let curTime = (Date.now() - start) / 1000;
                        console.log('Play: Timeout seconds: ', curTime);
                        console.log('play: first_loop:', x);
                        gaugePS1L.value = data_QTOT1[x];
                        gaugePS1R.value = data_QTOT2[x];

                        gaugePS2L.value = data_NH1[x];
                        gaugePS2R.value = data_NH2[x];

                        gaugePS3L.value = data_NPREQ1[x];
                        gaugePS3R.value =data_NPREQ2[x];

                        gaugePS4L.value = data_ITT1[x];
                        gaugePS4R.value = data_ITT2[x];

                        gaugePS5L.value = data_MOT1[x];
                        gaugePS5R.value = data_MOP1[x];

                        gaugePS6L.value = data_MOT2[x];
                        gaugePS6R.value = data_MOP2[x];
                       
                        big_watch.value=watch_data[x];
                        document.getElementById('seeker').value=x;

                        gaugeCLA1.value = cla1[x]
                        gaugeCLA2.value = cla2[x]
                        gaugePLA1.value = pla1[x]
                        gaugePLA2.value = pla2[x]

                        document.getElementById('ff_l').value=data_WF1[x];
                        document.getElementById('ff_r').value=data_WF2[x];
                        document.getElementById('nl_l').value=data_NL1[x];
                        document.getElementById('nl_r').value=data_NL2[x];

                        x++;
                                       
                    }, 1000);

    }


////////////////////////////////////////////////Get all control values//////////////////////////////////////////

function getControlValues() {
    if(true)
          {
            seekertempX.addEventListener("input", 
              function(){
                            tempX =seekertempX.value;
                        });
          }
    //else  {
            tempX = seekertempX.value;
         // }
            console.log('getControlValues: tempX,temp_watch', tempX);
        }
        
////////////////////////////////////////////////Pause//////////////////////////////////////////

 function pause(){
 debugger;
    //for button background
    document.getElementById("play_bgcolor").style.backgroundColor="#fff";
    document.getElementById("pause_bgcolor").style.backgroundColor=button_bgcolor;
    document.getElementById("stop_bgcolor").style.backgroundColor="#fff";
    document.getElementById("back_bgcolor").style.backgroundColor="#fff";
    document.getElementById("forward_bgcolor").style.backgroundColor="#fff";
    
    getControlValues();
    
    killIntervals();  
 }

////////////////////////////////////////////////Stop//////////////////////////////////////////

 function stop(){
 debugger;
    //for button background
    document.getElementById("play_bgcolor").style.backgroundColor="#fff";
    document.getElementById("pause_bgcolor").style.backgroundColor="#fff";
    document.getElementById("stop_bgcolor").style.backgroundColor=button_bgcolor;
    document.getElementById("back_bgcolor").style.backgroundColor="#fff";
    document.getElementById("forward_bgcolor").style.backgroundColor="#fff";
    //debugger;  

        gaugePS1L.value = metaQTOT.MIN_VALUE;
        gaugePS1R.value = metaQTOT.MIN_VALUE;
        gaugePS2L.value = metaNH.MIN_VALUE;
        gaugePS2R.value = metaNH.MIN_VALUE;
        gaugePS3L.value = metaNPREQ.MIN_VALUE;
        gaugePS3R.value = metaNPREQ.MIN_VALUE;
        gaugePS4L.value = metaITT.MIN_VALUE;
        gaugePS4R.value = metaITT.MIN_VALUE;
        gaugePS5L.value = metaMOT.MIN_VALUE;
        gaugePS5R.value = metaMOP.MIN_VALUE;
        gaugePS6L.value = metaMOT.MIN_VALUE;
        gaugePS6R.value = metaMOP.MIN_VALUE;

        big_watch.value = metaTime.minTime;
        document.getElementById('seeker').value = metaTime.minTime;

        gaugeCLA1.value = 0;
        gaugeCLA2.value = 0;
        gaugePLA1.value = 0;
        gaugePLA2.value = 0;

        document.getElementById('ff_l').value = 0;
        document.getElementById('ff_r').value = 0;
        document.getElementById('nl_l').value = 0;
        document.getElementById('nl_r').value = 0;

        getControlValues();
        killIntervals();
 }
       
////////////////////////////////////////////////backward//////////////////////////////////////////

function backward(){ 
debugger;
  //for button background
  document.getElementById("play_bgcolor").style.backgroundColor="#fff";
  document.getElementById("pause_bgcolor").style.backgroundColor="#fff";
  document.getElementById("stop_bgcolor").style.backgroundColor="#fff";
  document.getElementById("back_bgcolor").style.backgroundColor=button_bgcolor;
  document.getElementById("forward_bgcolor").style.backgroundColor="#fff";
        let start = Date.now();
        getControlValues();
        killIntervals();

  //debugger;
      //var tempX=localStorage.getItem('temp');
        console.log('Rewind: tempX', tempX);
        i = tempX;
        myGuageInterval = setInterval(() => {
            if (i < 0) {
                clearInterval(myGuageInterval);
                console.log('Rewind: end of guage loop');
                return;
            }

            let curTime = (Date.now() - start) / 1000;
            console.log('Rewind: Timeout seconds: ', curTime);
            console.log('Rewind: first_loop:', i);

                    gaugePS1L.value = data_QTOT1[i];
                    gaugePS1R.value = data_QTOT2[i];

                    gaugePS2L.value = data_NH1[i];
                    gaugePS2R.value = data_NH2[i];

                    gaugePS3L.value = data_NPREQ1[i];
                    gaugePS3R.value =data_NPREQ2[i];

                    gaugePS4L.value = data_ITT1[i];
                    gaugePS4R.value = data_ITT2[i];

                    gaugePS5L.value = data_MOT1[i];
                    gaugePS5R.value = data_MOP1[i];

                    gaugePS6L.value = data_MOT2[i];
                    gaugePS6R.value = data_MOP2[i]; 

                document.getElementById('seeker').value=i;
                big_watch.value=watch_data[i];

                gaugeCLA1.value = cla1[i];
                gaugeCLA2.value = cla2[i];
                gaugePLA1.value = pla1[i];
                gaugePLA2.value = pla2[i];

                document.getElementById('ff_l').value = data_WF1[i];
                document.getElementById('ff_r').value = data_WF2[i];
                document.getElementById('nl_l').value=data_NL1[i];
                document.getElementById('nl_r').value=data_NL2[i];

          i--;

        }, 300);     

}

///////////////////////////////////////////forward////////////////////////////////////////////

function forward(){
debugger;
  //for button background
  document.getElementById("play_bgcolor").style.backgroundColor="#fff";
  document.getElementById("pause_bgcolor").style.backgroundColor="#fff";
  document.getElementById("stop_bgcolor").style.backgroundColor="#fff";
  document.getElementById("back_bgcolor").style.backgroundColor="#fff";
  document.getElementById("forward_bgcolor").style.backgroundColor=button_bgcolor;
  //debugger;
  
        getControlValues();
        killIntervals();
        var n = watch_data.length - tempX;
        console.log('Forward: tempX', tempX);

        i = tempX;
        let start = Date.now();

          myGuageInterval = setInterval(function () {
              if (i >= watch_data.length) {
                  clearInterval(myGuageInterval);
                  console.log('Forward: end of guage loop');
                  return;
              }

              let curTime = (Date.now() - start) / 1000;
              console.log('Forward: Timeout seconds: ', curTime);
              console.log('Forward: first_loop:', i);
                    gaugePS1L.value = data_QTOT1[i];
                    gaugePS1R.value = data_QTOT2[i];

                    gaugePS2L.value = data_NH1[i];
                    gaugePS2R.value = data_NH2[i];

                    gaugePS3L.value = data_NPREQ1[i];
                    gaugePS3R.value =data_NPREQ2[i];

                    gaugePS4L.value = data_ITT1[i];
                    gaugePS4R.value = data_ITT2[i];

                    gaugePS5L.value = data_MOT1[i];
                    gaugePS5R.value = data_MOP1[i];

                    gaugePS6L.value = data_MOT2[i];
                    gaugePS6R.value = data_MOP2[i]; 

                    document.getElementById('seeker').value=i;
                    big_watch.value=watch_data[i]; 

                    gaugeCLA1.value = cla1[i];
                    gaugeCLA2.value = cla2[i];
                    gaugePLA1.value = pla1[i];
                    gaugePLA2.value = pla2[i];
                    
                    document.getElementById('ff_l').value = data_WF1[i];
                    document.getElementById('ff_r').value = data_WF2[i];
                    document.getElementById('nl_l').value=data_NL1[i];
                    document.getElementById('nl_r').value=data_NL2[i];
                    
             i++;
          }, 300); 
   
         }
////////////////////////////////////////////////kill Intervals//////////////////////////////////////////

        function killIntervals() {
            console.log('killIntervals: ');
            if (myGuageInterval) {
                clearInterval(myGuageInterval);
                myGuageInterval = null;
            }
        }

    </script>
    </body>
    </html>
        
        '''
        html = html.replace('bootvar', boot_var)
        html = html.replace('fontvar', font_var)
        html = html.replace('scriptjvar', script_jvar)
        html = html.replace('scriptbootvar', script_bootvar)
        html = html.replace('scriptgauge', script_gauge)
        html = html.replace('EEC1QTOT', eec1_qtot)
        html = html.replace('EEC2QTOT', eec2_qtot)
        html = html.replace('EEC1NH', eec1_nh)
        html = html.replace('EEC2NH', eec2_nh)
        html = html.replace('EEC1NPREQ', eec1_npreq)
        html = html.replace('EEC2NPREQ', eec2_npreq)
        html = html.replace('EEC1ITT', eec1_itt)
        html = html.replace('EEC2ITT', eec2_itt)
        html = html.replace('EEC1MOT', eec1_mot)
        html = html.replace('EEC2MOT', eec2_mot)
        html = html.replace('EEC1MOP', eec1_mop)
        html = html.replace('EEC2MOP', eec2_mop)
        html = html.replace('EEC1PLA', eec1_pla)
        html = html.replace('EEC2PLA', eec2_pla)
        html = html.replace('EEC1NL', eec1_nl)
        html = html.replace('EEC2NL', eec2_nl)
        html = html.replace('EMU1WF', emu1_wf)
        html = html.replace('EMU2WF', emu2_wf)
        html = html.replace('PEC1CLA', pec1_cla)
        html = html.replace('PEC2CLA', pec2_cla)
        html = html.replace('imagename', image_name)
        html = html.replace('digitalClock', digital_clock)
        html = html.replace('meta_QTOT', meta_qtot)
        html = html.replace('meta_NH', meta_nh)
        html = html.replace('meta_NPREQ', meta_npreq)
        html = html.replace('meta_ITT', meta_itt)
        html = html.replace('meta_MOT', meta_mot)
        html = html.replace('meta_MOP', meta_mop)
        html = html.replace('meta_WF', meta_wf)
        html = html.replace('meta_NL', meta_nl)
        html = html.replace('timeMinMax', time_min_max)
        html = html.replace('bombardierWidth', bombardier_width)
        html = html.replace('backwardimage', backward_image)
        html = html.replace('stopimage', stop_image)
        html = html.replace('pauseimage', pause_image)
        html = html.replace('forwardimage', forward_image)
        html = html.replace('playimage', play_image)
        html = html.replace('gaugeminpath', gauge_minpath)
        html = html.replace('bootstrappath', bootstrap_path)
        return html
    except Exception as e:
        logger.error(str(e))
        display_status(window, "Error with simulation Window")
    logger.info('Exit from  Gauge function')


class Ui(QMainWindow):
    """ ui code """
    logger.info("Entered into Ui class")

    def __init__(self):
        super(Ui, self).__init__()
        QMainWindow.__init__(self)
        uic.loadUi('script/discrete_EMU_Data_Viz.ui', self)
        #self.setFixedSize(self.size())
        fetch = get_report_details()
        if fetch:
            self.comboBox.addItems(fetch)  # here combobox automatically come here
        # Fetching the AirCraft details from DB
        values = load_air_craft()
        self.label_4.setText(values[1])
        self.label_5.setText(values[2])
        self.label_7.setText(values[4])
        self.label_9.setText(values[3])
        self.pushButton.clicked.connect(self.add_report_by_name)  # click add report popup window will come
        self.pushButton_2.clicked.connect(self.save_report)  # edit report
        self.comboBox.currentIndexChanged.connect(self.edit_report_by_name)
        self.pushButton_3.clicked.connect(self.delete_report_by_name)  # delete report
        self.pushButton_4.clicked.connect(self.push_button_4_open_click)  # graph
        self.pushButton_5.clicked.connect(self.push_button_5_open_click)  # simulation
        self.actionData_Load.triggered.connect(self.file_data_load)
        self.actionExit.triggered.connect(self.app_exit)
        self.actionAbout.triggered.connect(self.app_about)
        self.actionHelp_Manual.triggered.connect(self.help_manual)  # here we add about to help manual enquiry details
        self.show()
    logger.info("Exit from __init__ function")

    def save_report(self):
        """ for saving report """
        logger.info("Entered into save_report")
        conn1 = connect('script/EMU_DATA.db')
        message1 = QtWidgets.QMessageBox()
        try:
            param_list = []
            i = 0
            add_count = 0
            report_name = self.comboBox.currentText()
            if report_name != 'Select Report':
                while model.item(i):
                    if model.item(i).checkState():
                        di = dict()
                        di['filename'] = model.item(i).text()[:4]
                        di['parameter'] = model.item(i).text()[5:].split(':')[0]
                        di['discrete'] = ''
                        add_count += 1
                        param_list.append(di)
                    elif model.item(i).rowCount() > 0:
                        for c in range(0, model.item(i).rowCount()):
                            if model.item(i).child(c).checkState():
                                di = dict()
                                di['filename'] = model.item(i).text()[:4]
                                di['parameter'] = model.item(i).child(c).text()
                                di['discrete'] = model.item(i).text()[5:].split(':')[0]
                                add_count += 1
                                param_list.append(di)
                    i += 1
                now = dt.now()
                save_time = now.strftime('%Y-%m-%d %H:%M:%S')

                if add_count == 0:
                    message1.warning(self, "EMU Data Visualization",
                                     "Please select at least 1 parameter to save report")

                elif 0 < add_count <= 10:
                    cur = conn1.cursor()
                    cur.execute("DELETE FROM SAVED_REPORT_LIST where `REPORTNAME` = ? ;", (report_name,))
                    for param in param_list:
                        query = """INSERT INTO SAVED_REPORT_LIST (REPORTNAME, FILENAME, PARAMETER_STRING,
                                       REPORT_SAVE_TIME, DISCRETEFLAG) VALUES (?, ?, ?, ?, ?)"""

                        cur.execute(query, (report_name, param['filename'],
                                            param['parameter'], save_time, param['discrete']))
                    conn1.commit()
                    success = 'The Report "%s" has been successfully updated.' % report_name
                    message1.information(self, "EMU Data Visualization", success)
                    fetch = get_report_details()
                    self.comboBox.clear()
                    if fetch:
                        self.comboBox.addItems(fetch)
                elif add_count > 10:
                    msg = "The maximum number of parameters allowed is 10. You have selected {} parameters." \
                        .format(add_count)
                    message1.warning(self, "EMU Data Visualization", msg)

            else:
                message1.warning(self, "EMU Data Visualization", "Please select the Report that need to be changed.")

        except Exception as e:
            logger.error(str(e))
        finally:
            conn1.close()
        logger.info("Exit from save_report function")

    def edit_report_by_name(self):
        """ for editing report """
        logger.info("Entering into edit_report_by_name Function")
        conn2 = connect('script/EMU_DATA.db')
        try:
            cur = conn2.cursor()
            cur.execute("""SELECT `FILENAME`, `PARAMETER_STRING`, `DISCRETEFLAG` 
                            FROM SAVED_REPORT_LIST WHERE `REPORTNAME` =
                            ?;""", (self.comboBox.currentText(), ))
            fetch = cur.fetchall()
            params = []
            dis_params = []
            for param in fetch:
                cur.execute("""SELECT DESCRIPTION from MASTER_PARAMETER_LIST WHERE 
                                `FLIENAME` = ? AND `PARAMETER_NAME`= ?;""", (param[0][:-1], param[1]))
                res = cur.fetchone()
                if res is not None:
                    row = '%s_%s:%s' % (param[0], param[1], res[0])
                    params.append(row)
                else:
                    row = '%s_%s' % (param[0], param[2])
                    dis_params.append(row)
            i = 0
            while model.item(i):
                model.item(i).setCheckState(QtCore.Qt.Unchecked)
                model.item(i).setCheckState(QtCore.Qt.Unchecked)
                if model.item(i).text() in params:
                    model.item(i).setCheckState(QtCore.Qt.Checked)
                    model.item(i).setCheckState(QtCore.Qt.Checked)
                elif model.item(i).rowCount() > 0:
                    mas = model.item(i).text().split(':')[0]
                    selected_param = [sp[1] for sp in fetch if mas == sp[0] + '_' + sp[2]]
                    for c in range(0, model.item(i).rowCount()):
                        model.item(i).child(c).setCheckState(QtCore.Qt.Unchecked)
                        model.item(i).child(c).setCheckState(QtCore.Qt.Unchecked)
                        dis = model.item(i).child(c).text()
                        if mas in dis_params and dis in selected_param:
                            model.item(i).child(c).setCheckState(QtCore.Qt.Checked)
                            model.item(i).child(c).setCheckState(QtCore.Qt.Checked)
                i += 1
                self.treeView.setModel(model)
                self.treeView.setModel(model)
            return model
        except Exception as e:
            logger.error(str(e))
            display_status(window, "Error occured in database connection while Editing the report")
        finally:
            conn2.close()
        logger.info("Exit from ReportByName Function")

    def delete_report_by_name(self, text):
        """ for deleting report """
        logger.info("Entering into delete_report_by_name Function")
        conn3 = connect('script/EMU_DATA.db')
        message2 = QtWidgets.QMessageBox()
        try:
            cur = conn3.cursor()
            if self.comboBox.currentText() != 'Select Report':
                msg = 'Do you want to delete "%s" report?' % self.comboBox.currentText()
                button_reply = message2.question(self, 'EMU Data Visualization', msg, message2.Yes | message2.No)
                if button_reply == QMessageBox.Yes:
                    cur.execute("""DELETE FROM SAVED_REPORT_LIST WHERE `REPORTNAME`= ?;""",
                                (self.comboBox.currentText(),))
                    conn3.commit()
                else:
                    logger.info("Entering into else part of delete_report_by_name Function")
                fetch = get_report_details()
                self.comboBox.clear()
                if fetch:
                    self.comboBox.addItems(fetch)  # here combobox automatically come here
            else:
                message2.warning(self, "EMU Data Visualization", "Please select the Report that need to be Deleted.")
        except Exception as e:
            logger.error(str(e))
            display_status(window, "Error occured in database connection while deleting the report ")
        finally:
            conn3.close()
        logger.info("Exit from delete_report_by_name Function")

    def add_report_by_name(self):  # here open report popup window and give report name and insert in database
        """ for adding report name and save in database"""
        logger.info("Entering into AddReportName Function")
        conn4 = connect('script/EMU_DATA.db')
        message3 = QtWidgets.QMessageBox()
        try:
            param_list = []
            i = 0
            param_count = 0
            while model.item(i):
                if model.item(i).checkState():
                    di = dict()
                    di['filename'] = model.item(i).text()[:4]
                    di['parameter'] = model.item(i).text()[5:].split(':')[0]
                    di['discrete'] = ''
                    param_count += 1
                    param_list.append(di)
                elif model.item(i).rowCount() > 0:
                    for c in range(0, model.item(i).rowCount()):
                        if model.item(i).child(c).checkState():
                            di = dict()
                            di['filename'] = model.item(i).text()[:4]
                            di['parameter'] = model.item(i).child(c).text()
                            di['discrete'] = model.item(i).text()[5:].split(':')[0]
                            param_count += 1
                            param_list.append(di)
                i += 1
            now = dt.now()
            save_time = now.strftime('%Y-%m-%d %H:%M:%S')
            if param_count and param_count <= 10:
                report_name, ok_pressed = QInputDialog.getText(self, "EMU Data Visualization", "Report name:",
                                                               QLineEdit.Normal, "")
                conn4.row_factory = lambda cursor, row: row[0]
                cur = conn4.cursor()
                cur.execute("SELECT  DISTINCT `REPORTNAME` FROM SAVED_REPORT_LIST")
                saved_reports = cur.fetchall()
                if report_name:
                    if report_name and report_name not in saved_reports:
                        for param in param_list:
                            query = """INSERT INTO SAVED_REPORT_LIST (`REPORTNAME`, `FILENAME`, `PARAMETER_STRING`, 
                                        `REPORT_SAVE_TIME`, `DISCRETEFLAG`) VALUES (?, ?, ?, ?, ?)"""
                            cur.execute(query, (report_name, param['filename'], param['parameter'],
                                                save_time, param['discrete']))
                        conn4.commit()
                        success = 'The Report "%s" has been successfully saved.' % report_name
                        message3.information(self, "EMU Data Visualization", success)
                        fetch = get_report_details()
                        self.comboBox.clear()
                        if fetch:
                            self.comboBox.addItems(fetch)
                    else:
                        message = 'The Report "{}" already exists. Please save current report with another name.'\
                            .format(report_name)
                        message3.critical(self, "EMU Data Visualization", message)
                        del message
            elif param_count == 0:
                message3.warning(self, "EMU Data Visualization", "Please select at least 1 parameter to save a Report.")
            else:
                msg = "The maximum number of parameters allowed is 10. You have selected {} parameters."\
                    .format(param_count)
                message3.warning(self, "EMU Data Visualization", msg)
        except Exception as e:
            logger.error(str(e))
            display_status(window, "Error occured in database connection while add the report ")
        finally:
            conn4.close()
        logger.info("Exit from AddReprotName Function")

    @staticmethod
    def help_manual():
        """ here we have help manual functionality """
        logger.info("Entering into helpM_manual Function")
        try:
            help_manu.show()
        except Exception as e:
            logger.error(str(e))
            display_status(window, "unable to load help manual")
        logger.info("Exit from help_manual Function")

    # for graph
    def push_button_4_open_click(self):
        """ for display graph functionality """
        logger.info("Entering into pushButton_4_OpenClick Function")
        message4 = QtWidgets.QMessageBox()
        try:
            display_status(window, " Display Graph")
            param_list = []
            discrete_param_list = {}
            select_param = ""
            i = 0
            count = 0
            # Get the Parameters currently "checked"
            while model.item(i):
                if model.item(i).checkState():
                    count += 1
                    j = (model.item(i).text().find(":"))
                    select_param = select_param + model.item(i).text()[0:j] + ","
                    param_list.append(model.item(i).text()[0:j])
                elif model.item(i).rowCount() > 0:
                    li = []
                    for c in range(0, model.item(i).rowCount()):
                        if model.item(i).child(c).checkState():
                            count += 1
                            parent = model.item(i).text().split(':')[0]
                            child = model.item(i).child(c).text()
                            li.append(child+parent)
                    if any(li):
                        discrete_param_list[model.item(i).text().split(':')[0]] = li
                i += 1
            # display the Parameters as Graph
            if 0 < count <= 10:
                display_graph(param_list, discrete_param_list, self)
            elif count == 0:
                msg = "Please select at least 1 parameter to display a graph.."
                message4.warning(self, "EMU Data Visualization", msg)
            elif count > 10:
                msg = "The maximum number of parameters allowed is 10. You have selected {} parameters.".format(count)
                message4.warning(self, "EMU Data Visualization", msg)
        except Exception as e:
            logger.error(str(e))
            display_status(window, "unable to open graph")
        logger.info("Existing for pushButton_4_OpenClick Function")

    def push_button_5_open_click(self):
        """ for simulation functionality """
        logger.info("Entering into push_button_5_open_click function")
        try:
            json_object1 = json.loads(json_object())
            html = gauge_function(obj=json_object1)
            view2.setWindowTitle("EMU Data Cockpit Simulation by Tech Mahindra (Americas) Inc")
            view2.setHtml(html)
            size_object = QtWidgets.QDesktopWidget().screenGeometry(-1)
            width = size_object.width()
            height = size_object.height()
            view2.setGeometry(0, 30, width-1, height-55)
            view2.setWindowState((self.windowState() & ~Qt.WindowMinimized) | Qt.WindowActive)
            view2.raise_()
            view2.show()
        except Exception as e:
            logger.error(str(e))
            display_status(window, "Error in Simulation")
        logger.info("Existing for push_button_5_open_click function")

    def file_data_load(self):
        """ Process to load the data files for menu option File-> Data Load"""
        logger.info("Entering into  file_data_load Function")
        conn5 = connect('script/EMU_DATA.db')
        message5 = QtWidgets.QMessageBox()
        try:
            display_status(self, "Select any 1 csv file from folder")
            self.progressBar.setValue(0)
            dlg = QFileDialog()
            options = dlg.Options()
            options |= dlg.DontUseNativeDialog
            # get the file selected by user
            file_name, _ = dlg.getOpenFileName(self, "EMU Data Visualization", "", "CSV Files (*.csv)", options=options)
            if file_name:
                if validate_file_name_pattern(file_name) != 1:
                    message5.critical(window, 'EMU Data Visualization', "Please Select Valid csv file ( EMU / EEC / "
                                                                        "PEC )", message5.Ok)
                else:
                    display_status(window, "uploading...")
                    self.progressBar.setValue(25)
                    common_file_header = validate_file_headers(file_name)
                    if common_file_header == "N":
                        message5.critical(window, 'EMU Data Visualization', "File Header Information Mismatch",
                                          QMessageBox.Ok)
                        self.progressBar.setValue(0)
                    elif common_file_header == "F":
                        self.progressBar.setValue(0)
                    else:
                        # update the Incident Header Labels
                        headers = common_file_header.split("**")
                        self.label_9.setText(headers[0])
                        self.label_7.setText(headers[1])
                        self.label_4.setText(headers[2])
                        self.label_5.setText(headers[3])
                        self.progressBar.setValue(50)
                        # Load the Data to database
                        run_id = generate_run_id(conn5, window)
                        # get the file path and constant pattern
                        constant_pattern = file_name[0:len(file_name)-8]
                        save_master = save_batch_run_master(conn5, run_id, headers)
                        save_details = save_batch_details(conn5, run_id, constant_pattern)
                        if save_master == 1 and save_details == 1:
                            self.progressBar.setValue(100)
                            message5.information(self, "EMU Data Visualization", "All six data files have been "
                                                                                 "uploaded successfully")
                            display_status(window, " ")
                            self.progressBar.setValue(0)
        except Exception as e:
            logger.error(str(e))
            display_status(window, "Error with the database or csv file")
        logger.info("Exit from file_data_load Function")

    @staticmethod
    def app_exit():
        """ Closes the application for menu option File-> Exit"""
        logger.info("Entering into App_Exit")
        try:
            exit()
        except Exception as e:
            logger.error(str(e))
            display_status(window, "some internal  problem")
        logger.info("Existing for App_Exit Function")

    @staticmethod
    def app_about():
        """ Displays message about app version for menu option Help-> About"""
        logger.info("Entering into App_About Function")
        message6 = QtWidgets.QMessageBox()
        try:
            about_message = "Version 1.0.3" + "\n" + "CopyRight Tech Mahindra Ltd. 2018"
            message6.information(window, 'EMU Data Visualization', about_message, message6.Ok)
        except Exception as e:
            logger.error(str(e))
            display_status(window, "unable to open about some keyword missing")
        logger.info("Existing For App_About Function")


def load_air_craft():
    """ for loading details of aircraft """
    logger.info("Entering into load_air_craft Function")
    conn6 = connect('script/EMU_DATA.db')
    try:
        cur = conn6.cursor()
        air_craft_details = cur.execute("select * from BATCH_RUN_MASTER").fetchall()[0]
        return air_craft_details
    except Exception as e:
        logger.error(str(e))
        display_status(window, "Unable to load aircraft details")
    finally:
        conn6.close()
    logger.info("Existing for load_air_craft Function")


def discrete_plot(discrete_param_list):
    """ for plotting discrete parameters """
    logger.info("Entering into discrete_plot Function")
    conn7 = connect('script/EMU_DATA.db')
    try:
        cols = ['16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', '3', '2', '1']
        mainframe = DataFrame()
        for para in discrete_param_list:
            discretes = {i.split(':')[0]: i for i in discrete_param_list[para]}
            filename = 'DATA_' + para[:4]
            param = para[5:]
            data = read_sql('select `Time`, `' + param + '` from ' + filename, conn7)
            data = data[param].apply(lambda x: (int(float(x))))
            li = [list(bin(int(hex(i), 16))[2:].rjust(16, '0')) for i in data]
            df = DataFrame(li, columns=cols)
            for col in cols:
                if col not in discretes.keys():
                    df.drop(col, axis=1, inplace=True)
                else:
                    logger.info("Entering into else part of discrete_plot Function")
            df.rename(columns=discretes, inplace=True)
            mainframe = concat([mainframe, df], axis=1)
        return mainframe
    except Exception as e:
        logger.error(str(e))
        display_status(window, "unable to create dataframe for discrete")
    finally:
        conn7.close()
    logger.info("Existing into discrete_plot Function")


def get_report_details():  # add report functionality
    """ for getting report details """
    logger.info("Entering into getReportDetails Function")
    conn8 = connect('script/EMU_DATA.db')
    try:
        conn8.row_factory = lambda cursor, row: row[0]
        cur = conn8.cursor()
        cur.execute("SELECT DISTINCT `REPORTNAME` FROM SAVED_REPORT_LIST")
        fetch = cur.fetchall()
        fetch.insert(0, "Select Report")
        return fetch
    except Exception as e:
        logger.error(str(e))
        display_status(window, "database connection problem not fetching data")
    finally:
        conn8.close()
    logger.info("Existing into getReportDetails Function ")


def generate_run_id(conn, windo):
    """ generate Run_Id for table Batch_Run_Master (max Run_Id + 1)
    :param connection: sqlite connection
    :return: newRunId
    """
    logger.info("Entering into generate_run_id Function")
    conn9 = connect('script/EMU_DATA.db')
    try:
        cur = conn9.cursor()
        cur.execute("SELECT max(Run_id) FROM BATCH_RUN_MASTER ")
        run_master_rows = cur.fetchone()
        max_run_id = run_master_rows[0]
        if max_run_id is None:
            new_run_id = 1
        else:
            new_run_id = max_run_id + 1
        return new_run_id
    except Exception as e:
        logger.error(str(e))
        display_status(window, "run id not fetching through database")
    logger.info("Existing with generate_run_id Function")


def json_object():
    """ for return data as json from database """
    logger.info("Entering into json_object Function")
    conn9 = connect('script/EMU_DATA.db')
    try:
        object1 = {}
        sql_param_str1 = '''EEC1.`QTOT`, EEC1.`NH`, PEC1.`NPREQ`, PEC1.`NP(A)`, PEC1.`NP(B)`, EEC1.`ITT`, EMU1.`MOP`, 
        EEC1.`MOT`, EEC1.`PLA`, PEC1.`CLA`, EEC1.`NL`, EMU1.`WF`,'''
        sql_param_str2 = sql_param_str1.replace('1', '2')
        query1 = "select " + sql_param_str1 + """EMU1.time as EMUTime, PEC1.time as PECTime, 
                    EEC1.time as EECTime from data_emu1 as EMU1 
                    inner join data_emu2 as EMU2 on EMU1.record_number = EMU2.record_number 
                    inner join data_eec1 as EEC1 on EMU1.record_number = EEC1.record_number 
                    inner join data_eec2 as EEC2 on EMU1.record_number = EEC2.record_number 
                    inner join data_pec1 as PEC1 on EMU1.record_number = PEC1.record_number 
                    inner join data_pec2 as PEC2 on EMU1.record_number = PEC2.record_number"""
        query2 = "select " + sql_param_str2 + """ EMU1.time as EMUTime, PEC1.time as PECTime, 
                    EEC1.time as EECTime from data_emu1 as EMU1 
                    inner join data_emu2 as EMU2 on EMU1.record_number = EMU2.record_number 
                    inner join data_eec1 as EEC1 on EMU1.record_number = EEC1.record_number 
                    inner join data_eec2 as EEC2 on EMU1.record_number = EEC2.record_number 
                    inner join data_pec1 as PEC1 on EMU1.record_number = PEC1.record_number 
                    inner join data_pec2 as PEC2 on EMU1.record_number = PEC2.record_number"""
        values_query = '''SELECT * FROM SIMULATION_THRESHOLD'''
        df1 = read_sql_query(query1, conn9)
        df2 = read_sql_query(query2, conn9)
        df1['EMUTime'] = df1.EMUTime.fillna(0.0).astype(float).values.tolist()
        time_min_max = {'minTime': str(df1.EMUTime.min()), 'maxTime': str(df1.EMUTime.max())}
        object1['Time'] = df1['EMUTime'].values.tolist()
        df1['EMUTime'] = list(range(1, len(df1['EMUTime']) + 1))
        df2['EMUTime'] = list(range(1, len(df2['EMUTime']) + 1))
        # Calculated parameters
        # QTOT
        df1.QTOT = df1.QTOT.apply(lambda x: round((int(x) / 27680) * 100, 4))
        df2.QTOT = df2.QTOT.apply(lambda x: round((int(x) / 27680) * 100, 4))
        # NH
        df1.NH = df1.NH.apply(lambda x: round((float(x) / 27000) * 100, 4))
        df2.NH = df2.NH.apply(lambda x: round((float(x) / 27000) * 100, 4))
        # NL
        df1.NL = df1.NL.apply(lambda x: round((float(x) / 31300) * 100, 1))
        df2.NL = df2.NL.apply(lambda x: round((float(x) / 31300) * 100, 1))
        object1['EEC1QTOT'] = [int(val) if val > 0 else 0 for val in df1.QTOT.values.tolist()]
        object1['EEC2QTOT'] = [int(val) if val > 0 else 0 for val in df2.QTOT.values.tolist()]
        object1['EMU1WF'] = df1.WF.fillna(0.0).astype(float).values.tolist()
        object1['EMU2WF'] = df2.WF.fillna(0.0).astype(float).values.tolist()
        object1['EEC1NH'] = df1.NH.values.tolist()
        object1['EEC2NH'] = df2.NH.values.tolist()
        object1['EEC1NL'] = df1.NL.values.tolist()
        object1['EEC2NL'] = df2.NL.values.tolist()
        df1['NPmax'] = df1[["NP(A)", "NP(B)"]].max(axis=1)
        df2['NPmax'] = df2[["NP(A)", "NP(B)"]].max(axis=1)
        df1.NPmax = df1.NPmax.apply(lambda x: int(round((float(x) * 1020) / 100, 4)))
        df2.NPmax = df2.NPmax.apply(lambda x: int(round((float(x) * 1020) / 100, 4)))
        object1['EEC1NPREQ'] = df1.NPmax.values.tolist()
        object1['EEC2NPREQ'] = df2.NPmax.values.tolist()
        object1['EEC1ITT'] = df1.ITT.fillna(0.0).astype(float).values.tolist()
        object1['EEC2ITT'] = df2.ITT.fillna(0.0).astype(float).values.tolist()
        object1['EEC1MOP'] = df1.MOP.fillna(0.0).astype(float).values.tolist()
        object1['EEC2MOP'] = df2.MOP.fillna(0.0).astype(float).values.tolist()
        object1['EEC1MOT'] = [int(float(i)) for i in df1.MOT.values.tolist()]
        object1['EEC2MOT'] = [int(float(i)) for i in df2.MOT.values.tolist()]
        object1['EEC1PLA'] = df1.PLA.fillna(0.0).astype(float).values.tolist()
        object1['EEC2PLA'] = df2.PLA.fillna(0.0).astype(float).values.tolist()
        object1['PEC1CLA'] = df1.CLA.fillna(0.0).astype(float).values.tolist()
        object1['PEC2CLA'] = df2.CLA.fillna(0.0).astype(float).values.tolist()
        object1['timeMinMax'] = time_min_max
        met = read_sql_query(values_query, conn9)
        met = met.to_dict('records')
        for i in met:
            meta = 'meta_' + i['PARAMETER_NAME']
            i.pop('PARAMETER_NAME')
            object1[meta] = i
        json_object1 = json.dumps(object1)
        return json_object1
    except Exception as e:
        logger.error(str(e))
        display_status(window, "some database and object problem")
    logger.info("Existing for json_object function")


def save_batch_run_master(conn, run_id, headers):
    """ save control record to table Batch_Run_Master
    :param conn: sqlite connection
    :param run_id: id number
    :param headers: headers name
    :return: 1 for success
    """
    logger.info("Entering into  save_batch_run_master Function")
    conn = connect('script/EMU_DATA.db')
    try:
        data = [[RunId, headers[2], headers[3], headers[0], headers[1], "test"]]
        batch_run_master_df = DataFrame(data, columns=['RUN_ID', 'AIRCRAFT_SN', 'AIRCRAFT_TAIL', 'TRACE',
                                                       'INCIDENT_TIME', 'LOAD_TIME'])
        batch_run_master_df.to_sql('BATCH_RUN_MASTER', con=conn, if_exists='replace', index=False)
        return 1
    except Exception as e:
        logger.error(str(e))
        display_status(window, "some aircraft detail problem")
    finally:
        conn.close()
    logger.info("Existing with save_batch_run_master function")


def read_units(conn, filename_pattern, filename):
    """ for reading data as units """
    logger.info("Entering into read_units Function")
    try:
        fi = filename_pattern+filename
        cur = conn.cursor()
        csv_file = open(fi, 'r')
        spam_reader = list(csv.reader(csv_file, delimiter=','))
        names_with_units = dict(zip(spam_reader[14][2:], spam_reader[16][2:]))
        for name in names_with_units:
            query = '''UPDATE MASTER_PARAMETER_LIST SET `UNITS` = ? WHERE `PARAMETER_NAME` = ?;'''
            cur.execute(query, (names_with_units[name], name))
        conn.commit()
    except Exception as e:
        logger.error(str(e))
        display_status(window, "database connection problem")
    logger.info("Existing with read_units Functions")


def save_batch_details(conn, run_id, filename_pattern):
    """ save detail records to 6 table
        This need to be modified
        :param conn: sqlite connection
        :param run_id: id number
        :param filename_pattern: file name
        :return: 1 for success
    """
    logger.info("Entering into save_batch_details Connection Functionality")
    conn = connect('script/EMU_DATA.db')
    try:
        columns = {}
        query = "select distinct(fliename) from MASTER_PARAMETER_LIST;"
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        cur.execute(query)
        file_names = cur.fetchall()
        for filename in file_names:
            two_params = ['Names', 'Time']
            cur.execute("SELECT `PARAMETER_NAME` from MASTER_PARAMETER_LIST WHERE `FLIENAME` = ?;", (filename,))
            column = cur.fetchall()
            two_params.extend(column)
            columns[filename] = two_params
    except Exception as e:
        logger.error(str(e))
        display_status(window, "connection problem")
    try:
        logger.info("Entering into saveBatchDetails Function CSV validation Purpose")
        # Read Units
        read_units(conn, filename_pattern, "EMU1.csv")
        # Read EMU1 csv and write to database
        emu1_df = read_csv(filename_pattern + "EMU1.csv", names=columns['EMU'], dtype='str', header=17)
        # Remove the first column
        record_number = list(range(1, len(emu1_df['Time'])+1))
        del emu1_df['Names']
        emu1_df['Run_Id'] = run_id
        emu1_df['record_number'] = record_number
        emu1_df.to_sql('DATA_EMU1', con=conn, if_exists='replace', index=False)
        # Read EMU2 csv and write to database
        emu2_df = read_csv(filename_pattern + "EMU2.csv", names=columns['EMU'], dtype='str', header=17)
        # Remove the first column
        record_number = list(range(1, len(emu2_df['Time'])+1))
        del emu2_df['Names']
        emu2_df['Run_Id'] = run_id
        emu2_df['record_number'] = record_number
        emu2_df.to_sql('DATA_EMU2', con=conn, if_exists='replace', index=False)
        # Read EEC1 csv and write to database
        eec1_df = read_csv(filename_pattern + "EEC1.csv", names=columns['EEC'], dtype='str', header=17)
        read_units(conn, filename_pattern, "EEC1.csv")
        # Remove the first column
        record_number = list(range(1, len(eec1_df['Time'])+1))
        del eec1_df['Names']
        eec1_df['Run_Id'] = run_id
        eec1_df['record_number'] = record_number
        eec1_df.to_sql('DATA_EEC1', con=conn, if_exists='replace', index=False)
        # Read EEC2 csv and write to database
        eec2_df = read_csv(filename_pattern+"EEC2.csv", names=columns['EEC'], dtype='str', header=17)
        # Remove the first column
        record_number = list(range(1, len(eec2_df['Time']) + 1))
        del eec2_df['Names']
        eec2_df['Run_Id'] = run_id
        eec2_df['record_number'] = record_number
        eec2_df.to_sql('DATA_EEC2', con=conn, if_exists='replace', index=False)
        # Read PEC1 csv and write to database
        pec1_df = read_csv(filename_pattern + "PEC1.csv", names=columns['PEC'], dtype='str', header=17)
        read_units(conn, filename_pattern, "PEC1.csv")
        record_number = list(range(1, len(pec1_df['Time']) + 1))
        # Remove the first column
        del pec1_df['Names']
        pec1_df['Run_Id'] = run_id
        pec1_df['record_number'] = record_number
        pec1_df.to_sql('DATA_PEC1', con=conn, if_exists='replace', index=False)
        # Read PEC2 csv and write to database
        pec2_df = read_csv(filename_pattern + "PEC2.csv", names=columns['PEC'], dtype='str', header=17)
        # Remove the first column
        record_number = list(range(1, len(pec2_df['Time']) + 1))
        del pec2_df['Names']
        pec2_df['Run_Id'] = run_id
        pec2_df['record_number'] = record_number
        pec2_df.to_sql('DATA_PEC2', con=conn, if_exists='replace', index=False)
        return 1
    except Exception as e:
        logger.error(str(e))
        display_status(window, "csv file problem")
    logger.info("Existing with save_batch_details Function")


def validate_file_name_pattern(filename):
    """ Validates the format of filename selected
    :filename: Name of file selected by user
    :return:  1 for valid 0 for invalid filename pattern
    """
    logger.info("Entering into validate_file_name_pattern Function")
    try:
        if len(filename) > 8:
            file_pattern = filename[len(filename)-8:]
            if file_pattern in ["EMU1.CSV", "EMU2.CSV", "EEC1.CSV", "EEC2.CSV", "PEC1.CSV", "PEC2.CSV"]:
                pattern = 1
            else:
                pattern = 0
        else:
            pattern = 0
        return pattern
    except Exception as e:
        logger.error(str(e))
        display_status(window, "csv file name error")
    logger.info("Existing with validate_file_name_pattern function")


def validate_file_headers(filename):
    """ Validates the format of filename selected
    :filename: Name of file selected by user
    :return:  1 for valid 0 for invalid filename pattern
    """
    logger.info("Entering into validate_file_headers function")
    try:
        constant_pattern = filename[0:len(filename)-8]
        emu1_header = read_header_data(constant_pattern + "EMU1.CSV")
        emu2_header = read_header_data(constant_pattern + "EMU2.CSV")
        eec1_header = read_header_data(constant_pattern + "EEC1.CSV")
        eec2_header = read_header_data(constant_pattern + "EEC2.CSV")
        pec1_header = read_header_data(constant_pattern + "PEC1.CSV")
        pec2_header = read_header_data(constant_pattern + "PEC2.CSV")

        if emu1_header is None or emu2_header is None or eec1_header is None or eec2_header is None or pec1_header is \
                None or pec2_header is None:
            return "F"
        if emu1_header == emu2_header and emu2_header == eec1_header and eec1_header == eec2_header and eec2_header == \
                pec1_header and pec2_header == pec1_header:
            header = emu1_header
        else:
            header = "N"
        return header
    except Exception as e:
        logger.error(str(e))
        display_status(window, "file header mismatch")
    logger.info("Existing with validate_file_headers Function")


def read_header_data(input_file):
    """ Reads a file
    :input_file: Name of file to be read
    :return:  Header data for successful read , None for FileNotFoundError
    """
    logger.info("Entering into read_header_data Function ")
    try:
        f = open(input_file)
        i = 1
        for line in f:
            if i == 2:
                this_trace = line[6:].strip()
            if i == 4:
                this_time = line[10:].strip()
            if i == 11:
                this_aircraft_sn = line[12:].strip()
            if i == 12:
                this_aircraft_tail = line[21:].strip()
            if i == 15:
                this_column_headers = line.strip()
            i = i + 1
        f.close()
        this_header_values = this_trace + "**" + this_time + "**" + this_aircraft_sn + "**" + this_aircraft_tail
        # check whether EMU or EEC or PEC
        this_file_type = input_file[len(input_file) - 8: len(input_file) - 5]
        if validate_column_header(this_file_type, this_column_headers) == 0:
            return None
        logger.info("Existing with read_header_data Function")
        return this_header_values

    except Exception as e:
        logger.error(str(e))
        name = str(e).split('/')[-1].replace("'", '')
        msg = "Data File is Missing! Cannot find '%s'" % name
        display_status(window, msg)
        return None


class HelpManuals(QMainWindow):
    """ for showing details of help manual """
    logger.info("Entering into HelpManuals Class ")

    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self)
        self.setWindowTitle("EMU Data Visualization")
        self.setGeometry(170, 60, 915, 750)
        self.setFixedSize(self.size())
        self.view = QWebEngineView()
        self.setCentralWidget(self.view)
        url = QtCore.QUrl()
        self.view.setUrl(url.fromLocalFile(path.join(getcwd(), 'script/HelpManual.html')))
    logger.info("Existing with HelpManuals Class")


class GraphUi(QtWidgets.QMainWindow):
    """ for placing the print button on graph window """
    logger.info("Entering into GraphUi Class")

    def __init__(self):
        super(GraphUi, self).__init__()
        uic.loadUi('script/Airlines.ui', self)
        size_object = QtWidgets.QDesktopWidget().screenGeometry(-1)
        self.width = size_object.width()
        self.height = size_object.height()
        self.left = 0
        self.top = 30
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.pushButton.clicked.connect(self.graph_ui_print_pdf)
        
    def graph_ui_print_pdf(self):
        """ for printing graph as pdf """
        logger.info("Entering into graph_ui_print_pdf function")
        dlg = QFileDialog()
        options = dlg.Options()
        pdf_name, ok = dlg.getSaveFileName(self, "Save As", "", "All Files (*.pdf)", options=options)
        saved_name = path.basename(pdf_name)
        if ok:
            view.page().printToPdf('%s' % pdf_name)
            message7 = QtWidgets.QMessageBox()
            success = 'The graph has been saved successfully as %s' % saved_name
            message7.information(self, "EMU Data Visualization", success)
        else:
            logger.info("Entering into else part of graph_ui_print_pdf Function")
    logger.info("Existing with GraphUi Class")


def display_graph(this_param_list, discrete_param_list, self):
    """ Display Graph
    :paramlist : List of selected Masterlist Parameters
    :return:  None
    """
    logger.info("Entering into display_graph function")
    conn = connect('script/EMU_DATA.db')
    try:
        size_object = QtWidgets.QDesktopWidget().screenGeometry(-1)
        width = size_object.width()
        height = size_object.height()
        if any(discrete_param_list):
            discrete_df = discrete_plot(discrete_param_list)
            dis_columns = list(discrete_param_list.values())
        else:
            dis_columns = []
        calc = {'NH': 27000, 'NL': 31300, 'QTOT': 27680}
        sql_param_final = ""
        # Generate the columns to be fetched from database in the form EMU1.WF as EMU1_WF,
        # EMU2.WF as EMU2_WF
        for sql_param in this_param_list:
            sql_param_final = sql_param_final + sql_param[0:4] + ".`" + sql_param[5: len(sql_param)] + "` as `" + \
                              sql_param + "`, "
        grapf_data_df = read_sql("select " + sql_param_final + " EMU1.time as EMUTime, PEC1.time as PECTime, EEC1.time "
                                                               "as EECTime from data_emu1 as EMU1 inner join data_emu2 "
                                                               "as EMU2 on EMU1.record_number = EMU2.record_number "
                                                               "inner join data_eec1 as EEC1 on EMU1.record_number = "
                                                               "EEC1.record_number inner join data_eec2 as EEC2 on "
                                                               "EMU1.record_number = EEC2.record_number inner join "
                                                               "data_pec1 as PEC1 on EMU1.record_number = PEC1.record_"
                                                               "number inner join data_pec2 as PEC2 on EMU1.record_"
                                                               "number = PEC2.record_number""", conn)
        plotly_data = []
        layout_kwargs = {'title': 'Visualization of EMU Parameters',
                         'showlegend': 'True',
                         'xaxis': {'title': 'Time(Secs)',
                                   'titlefont': {'size': 18, 'color': 'rgb(175, 19, 100)'},
                                   'rangeslider': {'visible': True}
                                   }
                         }
        this_list = [pa[5:] for pa in this_param_list]
        setlist = list(dict.fromkeys(this_list))
        final = []
        for j in setlist:
            if this_list.count(j) == 2:
                mi = [p for p in this_param_list if p.endswith(j)]
            else:
                mi = [p for p in this_param_list if p.endswith(j)]
            final.append(mi)
        i = 0
        cursor = conn.cursor()
        query = "select `PARAMETER_NAME`, `UNITS` from MASTER_PARAMETER_LIST;"
        cursor.execute(query)
        res = cursor.fetchall()
        units = dict(res)
        if any(dis_columns):
            final.extend(dis_columns)
        else:
            pass
        for paraml in final:
            axis_name = 'yaxis' + str(i+1) * (i > 0)
            y_axis = 'y' + str(i+1) * (i > 0)
            for param in paraml:
                if param.split('_')[1] in calc.keys():
                    value = calc.get(param.split('_')[1])
                    grapf_data_df[param] = grapf_data_df[param].apply(lambda x: round((int(x) / value) * 100, 4))
                else:
                    logger.info("Entering into else part of display_graph Function")
                if param in grapf_data_df.columns.values:
                    plot_param = grapf_data_df[param]
                    x_param = grapf_data_df[param[:3]+'Time']
                    rang = {'autorange': True}
                else:
                    fil_name = [i[:3] for i in discrete_param_list.keys()]
                    param_name = [i for i in discrete_param_list.keys()]
                    plot_param = discrete_df[param]
                    rang = {'range': [0, 1], 'autorange': False, 'nticks': 5}
                    x_param = grapf_data_df[fil_name[0]+'Time']
                    param = [i + param.split(i)[0] for i in param_name if i in param][0]
                uni = param.split('_')[1] if '_' in param else param
                unit = units.get(uni, '').capitalize() if units.get(uni) else ''
                trace = go.Scatter(x=x_param,
                                   y=plot_param,
                                   name=param,
                                   yaxis=y_axis
                                   )
                plotly_data.append(trace)
            if i % 2 == 0:
                layout_kwargs[axis_name] = {'side': 'left',
                                            'color': 'rgb(205, 12, 24)',
                                            'domain': [(1/len(final)) * i, (1/len(final)) * (i+1)],
                                            'title': unit,
                                            'titlefont': {'size': 17, 'color': 'rgb(9, 18, 153)'}}

                layout_kwargs[axis_name].update(rang)

            else:
                layout_kwargs[axis_name] = {'side': 'right',
                                            'color': 'rgb(9, 18, 153)',
                                            'domain': [(1/len(final)) * i, (1/len(final))*(i+1)],
                                            'title': unit,
                                            'titlefont': {'size': 17, 'color': 'rgb(205, 12, 24)'}}
                layout_kwargs[axis_name].update(rang)
            i = i+1
        layout_1 = go.Layout(layout_kwargs, showlegend=True,
                             width=width-420, height=height-120,  # Graphline  Resizing
                             autosize=True,
                             legend=dict(orientation="h",
                                         x=0, y=-0.65,
                                         font=dict(family='sans-serif',
                                                   size=13,
                                                   color='#000'),
                                         bgcolor='rgb(220,220,220)',
                                         bordercolor='rgb(220,220,220)',
                                         borderwidth=1))
        conn = connect('script/EMU_DATA.db')
        cur = conn.cursor()
        cur.execute('select * from BATCH_RUN_MASTER')
        data = cur.fetchall()
        d = data
        st = 'Aircraft Serial No: {}                             Aircraft tail No: {} \
        <br><br>Incident Time: {}      Incident Trace: {}'.format(d[0][1],d[0][2],data[0][4],
                                                                                    data[0][3])
        updatemenus = list([
        dict(
            buttons=list([
                dict(
                    args=['type', ''],
                    label=st,
                    method='restyle'
                )
            ]),
            direction='left',
            pad={'r': 10, 't': -5},
            showactive=True,
            type='buttons',
            x=.25,
            xanchor='left',
            y=1.5,
            yanchor='top'
          ),
        ])
        layout_1['updatemenus'] = updatemenus        
        fig = go.Figure(data=plotly_data, layout=layout_1)
        config = {
            'showLink': False,
            'scrollZoom': True,
            'displayModeBar': True,
            'editable': False,
            'displaylogo': False,
            'modeBarButtonsToRemove': ['zoom2d', 'toImage', 'pan2d', 'sendDataToCloud', 'hoverClosestCartesian',
                                       'toggleSpikelines'],
            'autosizable': False
        }
        fn = path.join(getcwd(), 'script/stacked-subplots-shared-x-axis.html')
        plotly.offline.plot(fig, config=config, filename=fn, auto_open=False)
        graphs = ['xy', 'xy2', 'xy3', 'xy4', 'xy5', 'xy6', 'xy7', 'xy8', 'xy9', 'xy10']
        hover_functionality = '''javascriptstart[pointnumber
                           ],
                           numberofgraphs                     
                           );
               });</script></body></html>'''
        with open(path.join(getcwd(), 'script/stacked-subplots-shared-x-axis.html'), 'a+') as f:
            f.seek(0)
            html_file = f.read()
            html_file = html_file.strip('</script></body></html>')
            text = html_file.split('Plotly.animate(')[1].split(');})')[0]
        javascript_start = '''var myPlot = 
                        document.getElementById(textid);
                        myPlot.on('plotly_hover', function (eventdata) {
                        Plotly.Fx.hover(textid,'''.replace('textid', text)
        hover_functionality = hover_functionality.replace('javascriptstart', javascript_start)
        graphs = graphs[0:len(final)]
        hover_functionality = hover_functionality.replace('numberofgraphs', str(graphs))
        final_point_number = ''
        for i in range(len(this_list)):
            point_number = '{curveNumber: %s, pointNumber: eventdata.points[0].pointNumber},' % str(i)
            final_point_number += point_number
        hover_functionality = hover_functionality.replace('pointnumber', final_point_number)
        new_html = html_file + hover_functionality
        with open(path.join(getcwd(), 'script/stacked-subplots-shared-x-axis.html'), 'w') as html:
            html.write('<html><h')
            html.write(new_html)
        url1 = QtCore.QUrl()
        view.load(url1.fromLocalFile(fn))
        view.loadFinished.connect(GraphUi)
        self.graphWindow = GraphUi()
        view1 = self.graphWindow.webView
        view1.load(url1.fromLocalFile(fn))
        view1.setGeometry(10, 10, width-20, height-70)
        view1.setWindowState((self.windowState() & ~Qt.WindowMinimized) | Qt.WindowActive)
        view1.raise_()
        self.graphWindow.show()
    except Exception as e:
        logger.error(str(e))
        display_status(window, "Error occured while connecting to Database ")
    logger.info("Existing with display_graph Function")


def validate_column_header(file_type, column_header):
    """ Validate if the columns of the file are identical to the column list in FILE_METADATA
    :filetype: Type of file eg EMU, EEC, PEC
    :columnHeader : The column header from row 15 of the file
    :return:  1 for success 0 for failure
    """
    logger.info("Entering into validate_column_header function")
    message8 = QtWidgets.QMessageBox()
    try:
        DataFrame()
        this_query = "FILENAME=='" + file_type + "'"
        this_df = columnHeaders_df.query(this_query)

        if this_df.loc[this_df.index[0], 'COLUMN_VALUES'] == column_header:
            header_value = 1
        else:
            message8.information(window, 'EMU Data Visualization', 'The column format has been changed for data file '
                                 + file_type, message8.Ok)
            header_value = 0
        return header_value
    except Exception as e:
        logger.error(str(e))
        display_status(window, 'The column format has been changed for data file ' + file_type, message8.Ok)
    logger.info("Existing with validate_column_header Function")


def display_status(ui, status_message):
    """ Display statusMessage in the status bar of the Application Window
    :param ui: Application Window
    :param status_message : Message to be displayed
    :return:  None
    """
    logger.info("Entering into display_status function")
    try:
        ui.statusbar.showMessage(status_message)
    except Exception as e:
        logger.error(str(e))
        display_status(window, "display status bar keyword missing")
    logger.info("Existing with display_status Functions")


def create_connection(db_file):
    """ create a database connection to the SQLite database
    specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    logger.info("Entering into create_connection function")
    conn = connect('script/EMU_DATA.db')
    try:
        return conn
    except Exception as e:
        logger.error(str(e))
        display_status(window, "connection Problem")
    logger.info("Existing with create_connection Function")
    return None


def load_master_parameters(ui, conn):
    """ load the comboBox with data for MASTER_PARAMETER_LIST
        :param conn: sqlite connection
        :param defined1: Application Window
        :return: model QStandardItemModel
    """
    logger.info("Entering into load_master_parameters function")
    try:
        model = QStandardItemModel(ui.treeView)
        ui.treeView.setHeaderHidden(True)
        cur = conn.cursor()
        cur.execute("SELECT * FROM MASTER_PARAMETER_LIST WHERE DISPLAYFLAG =1")
        rows = cur.fetchall()
        for row in rows:
            # create an item with for each set of file
            item1 = QStandardItem(str(row[0]) + "1_" + str(row[1]) + ":" + str(row[2]))
            item2 = QStandardItem(str(row[0]) + "2_" + str(row[1]) + ":" + str(row[2]))
            # add child items for discrete parameters
            if str(row[4]) == "Y":
                # Create child cursor that fetches discrete column values from table DISCRETE_PARAMETER
                cur_child = conn.cursor()
                cur_child.execute("SELECT * FROM `DISCRETE_PARAMETER` WHERE `PARAMETER_NAME`='" + str(row[1]) + "'")
                rows_child = cur_child.fetchall()
                for child in rows_child:
                    # add child item for values of columns from value_1 to value_16
                    column_position = 16
                    for cols in range(2, 18):
                        # do not display discrete values "Not Used"
                        if str(child[cols]) != "Not used":
                            # Display Child items in the format Hexadecimal Position:Value Description
                            child_item1 = QStandardItem(str(column_position) + ":" + str(child[cols]))
                            child_item2 = QStandardItem(str(column_position) + ":" + str(child[cols]))
                            child_item1.setCheckable(True)
                            child_item1.setEditable(False)
                            child_item2.setCheckable(True)
                            child_item2.setEditable(False)
                            item1.appendRow(child_item1)
                            item1.setEditable(False)
                            item2.appendRow(child_item2)
                            item2.setEditable(False)
                        column_position = column_position - 1
            else:
                # add a checkbox to it
                item1.setCheckable(True)
                item1.setEditable(False)
                item2.setCheckable(True)
                item2.setEditable(False)
            # Add the item to the model
            if row[1] is not None:
                model.appendRow(item1)
                model.appendRow(item2)
        # Apply the model to the list view
        ui.treeView.setModel(model)
        return model
    except Exception as e:
        logger.error(str(e))
        display_status(window, "master parameter not uplod successfully")
    logger.info("Existing with load_master_parameters function")


if __name__ == '__main__':
    logger.info("Entering into main function")
    now = dt.now()
    to_date = dt.strptime(now.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
    start_date = dt.strptime('2018-11-09 00:00:00', '%Y-%m-%d %H:%M:%S')
    end_date = start_date + timedelta(days=7)    
    argv.append("--disable-web-security")
    app = QtWidgets.QApplication(argv)
    help_manu = HelpManuals()
    view = QWebEngineView()
    RunId = 0
    window = Ui()
   # window.resize(640, 480)
    display_status(window, " Please Load the Data files")
    database = "EMU_DATABASE.db"
    conn = create_connection(database)
    model = load_master_parameters(window, conn)
    columnHeaders_df = read_sql("select `FILENAME`, `COLUMN_VALUES` from FILE_METADATA", conn)
    view2 = QWebEngineView()
    if to_date < end_date:
        exit(app.exec_())
    else:
        buttonReply = QMessageBox.information(window, 'EMU Data Visualization', 'The validity of this Demo Version of '
                                                                                'Data Visualizer Application has '
                                                                                'expired.', QMessageBox.Ok)
        logger.info("The validity of this Demo version of Data Visualizer Application has expired.")
        if buttonReply == QMessageBox.Ok:
            window.close()
    logger.info("Existing with if __name__ == '__main__' function")

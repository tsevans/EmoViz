<!DOCTYPE html>
<html lang="en">
    <head>
        
        <!-- Basic Page Needs
         –––––––––––––––––––––––––––––––––––––––––––––––––– -->
        <meta charset="utf-8">
            <title>EmoViz Home</title>
            <meta name="description" content="">
                <meta name="author" content="">
                    
                    <!-- Mobile Specific Metas
                     –––––––––––––––––––––––––––––––––––––––––––––––––– -->
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                        
                        <!-- FONT
                         –––––––––––––––––––––––––––––––––––––––––––––––––– -->
                        <link href="https://fonts.googleapis.com/css?family=Tajawal" rel="stylesheet">
                            
                            <!-- CSS
                             –––––––––––––––––––––––––––––––––––––––––––––––––– -->
                            <link rel="stylesheet" href="css/normalize.css">
                                <link rel="stylesheet" href="css/skeleton.css">
                                    <link rel="stylesheet" href="css/custom.css">
                                        
                                        <!-- Scripts
                                         –––––––––––––––––––––––––––––––––––––––––––––––––– -->
                                        
                                        <!-- Favicon
                                         –––––––––––––––––––––––––––––––––––––––––––––––––– -->
                                        <link rel="icon" type="image/png" href="images/favicon1.png">
                                         
        <script type="text/javascript">
			function load_plot() {
				var php = "<" + "?" + "php printNameType();?>";
     			document.getElementById("plot-content").innerHTML= php + '<object type="text/html" data="radar_multi_1522708451.227119.html" style="height:100%; width:100%;" ></object>';
			}
			function reset_plots() {
     			document.getElementById("plot-content").innerHTML='&nbsp;';
			}
			function load_file(x) {
				var php = "<" + "?" + "php setFileName(" + x + ");?>";
				document.getElementById("plot-content-header").innerHTML= php;
			}
			function load_plot_type(x) {
				var php = "<" + "?" + "php setPlotType(" + x + ");?>";
				document.getElementById("plot-content-header").innerHTML= php;
			}
		</script>
        
        <style>
			@import url('https://fonts.googleapis.com/css?family=Tajawal');
		</style>
        
    </head>
    <body>
    	<?php
			$fileName = $plotType = $execCall = "";
			$fileCount = $errorFlag = 0;
			
			if ($_SERVER["REQUEST_METHOD"] == "POST") {
				
				$fileName = $_POST["fileName"];
				$plotType = $_POST["plotType"];
				
				if ($fileName != NULL) {
					foreach($fileName as $value1) {
						$fileCount++;
						$execCall .= $value1 . ' ';
					}
				}
				
				if ($fileCount == 0) {
					$execCall = "No files selected. Please select a data file to generate a visualization.";
					$errorFlag = 1;
				} elseif ($plotType == "") {
					$execCall = "No visualization type selected. Please select a visualization type to generate a visualization.";
					$errorFlag = 1;
				} else {
					if ($plotType == 'Radar') {
						if ($fileCount <= 5) {
							$execCall .= ' ' . $plotType;
						} else {
							$execCall = "You have selected too many data files for the Radar Visualization. Please select 1-5 data files and try again.";
							$errorFlag = 1;
						}
					} elseif ($plotType == 'Heat Map') {
						if ($fileCount == 1) {
							$execCall .= ' ' . $plotType;
						} else {
							$execCall = "You have selected too many data files for the Heat Map. Please select 1 data file and try again.";
							$errorFlag = 1;
						}
					} else {
						if ($fileCount == 1) {
							$execCall .= ' ' . $plotType;
						} else {
							$execCall = "You have selected too many data files for the Ribbon Visualization. Please select 1 data file and try again.";
							$errorFlag = 1;
						}
					}
				}
			}
			
		?>

        <!-- Primary Page Layout
         –––––––––––––––––––––––––––––––––––––––––––––––––– -->
        <div style="height: 10px; background-color: #01c6da; line-height: 10px;" >
        	&nbsp;
        </div>
        	<!--<img src="images/nav-logo1-white2.png" alt="EmoViz" height="120" width ="121">
            <div style="float: right; width: 130px;">
            	&nbsp;
            </div>
            <div class="nav-filters">
                    <h4 class="value-heading"><a href="#" onclick="reset_plots()">Disgust</a></h4>
            </div>
            <div class="nav-filters">
                    <h4 class="value-heading"><a href="#" onclick="reset_plots()">Scared</a></h4>
            </div>
            <div class="nav-filters">
                    <h4 class="value-heading"><a href="#" onclick="reset_plots()">Surprise</a></h4>
            </div>
            <div class="nav-filters">
                    <h4 class="value-heading"><a href="#" onclick="reset_plots()">Anger</a></h4>
            </div>
            <div class="nav-filters">
                    <h4 class="value-heading"><a href="#" onclick="reset_plots()">Sad</a></h4>
            </div>
            <div class="nav-filters">
                    <h4 class="value-heading"><a href="#" onclick="reset_plots()">Happy</a></h4>
            </div>
            <div class="nav-filters">
                    <h4 class="value-heading"><a href="#" onclick="reset_plots()">Neutral</a></h4>
            </div>
            <div class="nav-filters">
                    <h4 class="value-heading"><a href="#" onclick="reset_plots()">All</a></h4>
            </div>
        </div>-->
        
		<div style="height: 98.8vh; width: 121px; background-color: #ffb86b; float: left; margin-top: 0px;">
        	<img src="images/nav-logo1-white2.png" alt="EmoViz" height="120" width ="121">
            &nbsp;
        </div>
        
        <div class="container" style="margin-bottom: 0;">
        <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
            <div class="row" style="height: 528px;">
            <div class="three columns" style="border-style: solid; padding: 8px; margin: 0 20px 0 10px; border-color: #484f59; border-radius: 2px;" >
                    <!--<h3 class="section-heading">Data:</h3>-->
                    <div id="data-content" style="overflow: auto; height: 75vh; width: 100%">
                    Select at least one data file below: <br /><br />
                    	<!--<ul>
                    		<a href="" class="li-hover"><li>P01_Emotion.csv</li></a>
                            <a href="" class="li-hover"><li>P02_Emotion.csv</li></a>
                            <a href="" class="li-hover"><li>P03_Emotion.csv</li></a>
                            <a href="" class="li-hover"><li>P04_Emotion.csv</li></a>
                            <a href="" class="li-hover"><li>P05_Emotion.csv</li></a>
                            <a href="" class="li-hover"><li>P06_Emotion.csv</li></a>
                            <a href="" class="li-hover"><li>P07_Emotion.csv</li></a>
                            <a href="" class="li-hover"><li style="border: 0;">P08_Emotion.csv</li></a>
                    	</ul>-->
                        <?php
							$log_directory = 'data_proc/';
                            $results_array = array();
                            if (is_dir($log_directory)) {
        						if ($handle = opendir($log_directory)) {
                					while(($file = readdir($handle)) !== FALSE) {
                        				$results_array[] = $file; 
                                    }
                				closedir($handle);
        						}
							}
							foreach($results_array as $value) {
								if ($value != '.' && $value != '..') {
									$checked = "";
    								//echo '<a href="" onclick="load_file(' . $value . ')"><li>' . $value . '</li></a>';
									if ($fileName != NULL) {
										if (in_array($value, $fileName)) {
											$checked = " checked";
										}
									}
									echo '<input type="checkbox" name="fileName[]" value="' . $value . '"' . $checked .'>' . $value . '<br />';
								} 
                      		}				

						?>
                        <!-- onclick="load_file(\'' . $value . '\')"  -->
                    </div>
                </div>
                <div class="nine columns" style="border-style: solid; padding: 8px; margin-left: 0px; border-color: #484f59; border-radius: 2px;" >
                    <h3 class="section-heading" id="plot-content-header" style="float: left; position: fixed; z-index: 2000;">&nbsp;</h3>
                    <div id="plot-content" style="height: 75vh; width: 100%">
                    
        				<?php
							echo "<h2>Your Input:</h2> Files: ";
							if ($fileName != NULL) {
								foreach($fileName as $value1) {
									echo $value1 . ' ';
								}
							}
							echo "<br>";
							echo 'Plot type: ' . $plotType;
							echo "<br>";
							echo "Terminal command: " . $execCall;
							echo "<br>";
							echo "Error flag: " . $errorFlag;
							echo "<br>";
						?>    
                    </div>
                </div>
            </div>
                <div class="graph-choice">
                    <!--<h4 class="value-heading"><a href="#" onclick="reset_plots()">Line</a></h4>-->
                    <input type="radio" name="plotType" <?php if (isset($plotType) && $plotType=="Radar") echo "checked";?> value="Radar" class="button-primary" style="margin: 0;">Radar
            	</div>
                <div class="graph-choice">
                    <!--<h4 class="value-heading"><a href="#" onclick="reset_plots()">Radar</a></h4>-->
                    <input type="radio" name="plotType" <?php if (isset($plotType) && $plotType=="Heat Map") echo "checked";?> value="Heat Map" class="button-primary" style="margin: 0;">Heat Map
            	</div>
                <div class="graph-choice">
                    <!--<h4 class="value-heading"><a href="#" onclick="reset_plots()">Ribbon</a></h4>-->
                    <input type="radio" name="plotType" <?php if (isset($plotType) && $plotType=="Ribbon") echo "checked";?> value="Ribbon" class="button-primary" style="margin: 0;">Ribbon
            	</div>
                <input type="submit" name="submit" value="Generate" class="generate" style="color: green; padding: 5px 5px 0 8px;">
                <!--<div class="generate">
                    <h4 class="value-heading"><a style="color: green;" href="#" onclick="load_plot()">Generate</a></h4>
                    
            	</div>-->
        </form>    
        </div>
        <!--
        <div class="container">
            <div class="row">
                <div class="twelve columns" style="border-style: solid;" >
                    <h3 class="section-heading">Datasets will be selected from here.</h3>
                    <p style="height: 100px;">
                    	And here.
                    </p>
                </div>
            </div>
        </div>
        -->
        
              <!-- End Document
            –––––––––––––––––––––––––––––––––––––––––––––––––– -->
            </body>
</html>

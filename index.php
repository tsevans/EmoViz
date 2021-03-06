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
     			document.getElementById("plot-content").innerHTML = '<object type="text/html" data="radar_multi_1522264764.96.html" style="height:100%; width:100%;" ></object>';
				alert(1);
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
    <!-- PHP Logic, Setting Variables, Data Validation, Exec Call to Python
         –––––––––––––––––––––––––––––––––––––––––––––––––– -->
    	<?php
			$fileName = $plotType = $plotCode = $execCall = $vizName = "";
			$fileCount = 0;
			$errorFlag = -1;
			
			if ($_SERVER["REQUEST_METHOD"] == "POST") {
				
				$fileName = $_POST["fileName"];
				$plotType = $_POST["plotType"];
				
				if ($fileName != NULL) {
					foreach($fileName as $value1) {
						$fileCount++;
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
							$plotCode = 'RAD';
							$execCall .= ' ' . $plotCode . ' ';
							$errorFlag = 0;
						} else {
							$execCall = "You have selected too many data files for the Radar Visualization. Please select 1-5 data files and try again.";
							$errorFlag = 1;
						}
					} elseif ($plotType == 'Heat Map') {
						if ($fileCount == 1) {
							$plotCode = 'HMP';
							$execCall .= ' ' . $plotCode . ' ';
							$errorFlag = 0;
						} else {
							$execCall = "You have selected too many data files for the Heat Map. Please select 1 data file and try again.";
							$errorFlag = 1;
						}
					} elseif ($plotType == 'Line') {
						if ($fileCount <= 2) {
							$plotCode = 'LNG';
							$execCall .= ' ' . $plotCode . ' ';
							$errorFlag = 0;
						} else {
							$execCall = "You have selected too many data files for the Line Visualization. Please select 1-2 data files and try again.";
							$errorFlag = 1;
						}
					} else {
						if ($fileCount == 1) {
							$plotCode = 'RIB';
							$execCall .= ' ' . $plotCode . ' ';
							$errorFlag = 0;
						} else {
							$execCall = "You have selected too many data files for the Ribbon Visualization. Please select 1 data file and try again.";
							$errorFlag = 1;
						}
					}
				}
				
				$nums = "";
				
				if ($fileName != NULL && $errorFlag == 0) {
					foreach($fileName as $value1) {
						$list = explode("_", $value1);
						$nums .= $list[1] . '-';
						$execCall .= $value1 . ' ';
					}
					$nums = substr($nums, 0, -1);
				}
				
				if ($errorFlag == 0) {
					$vizName = '' . $plotCode . '_' . $nums . '.html';
					$send = "python main.py " . $execCall;
					exec($send);
				}
			}
			
		?>

        <!-- Primary Page Layout
         –––––––––––––––––––––––––––––––––––––––––––––––––– -->
        <div style="height: 10px; background-color: #01c6da; line-height: 10px;" >
        	&nbsp;
        </div>
        
		<div style="height: 98.8vh; width: 121px; background-color: #ffb86b; float: left; margin-top: 0px;">
        	<img src="images/nav-logo1-white2.png" alt="EmoViz" height="120" width ="121">
            &nbsp;
        </div>
        
        <div class="container" style="margin-bottom: 0;">
        <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
            <div class="row" style="height: 528px;">
            <div class="three columns" style="border-style: solid; padding: 8px; margin: 0 20px 0 10px; border-color: #484f59; border-radius: 2px;" >
            
                    <div id="data-content" style="overflow: auto; height: 75vh; width: 100%">
                    Select at least one data file below: <br /><br />
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
									if ($fileName != NULL) {
										if (in_array($value, $fileName)) {
											$checked = " checked";
										}
									}
									echo '<label class="check_contain">' . $value . '<input type="checkbox" name="fileName[]" value="' . $value . '"' . $checked .'><span class="checkmark"></span></label>';
								} 
                      		}				

						?>
                        
                    </div>
                </div>
                <div class="nine columns" style="border-style: solid; padding: 8px; margin-left: 0px; border-color: #484f59; border-radius: 2px;" >
                    <h3 class="section-heading" id="plot-content-header" style="float: left; position: fixed; z-index: 2000;">&nbsp;</h3>
                    <div id="plot-content" style="height: 75vh; width: 100%">
                    
        				<?php
						if ($errorFlag == 0) {
							libxml_use_internal_errors(true);
							$doc = new DOMDocument();
							$dir = 'plots/' . $vizName;
							$doc->loadHTMLFile($dir);
							echo '<p style="position: fixed; z-index: 2000;">';
							echo 'Files: ';
							if ($fileName != NULL) {
								foreach($fileName as $value1) {
									echo $value1 . ' ';
								}
							}
							echo '<br />Plot type: ' . $plotType;
							//echo '<br />Call: ' . $send;
							echo '</p>';
							echo $doc->saveHTML();
						} elseif ($errorFlag == 1) {
							echo '<h2 style="color: red;">Error: ' . $execCall . '</h2>';
						} else {
							echo '<h2>Please select data files to visualize.</h2>';
						}
						?>    
                    </div>
                </div>
            </div>
                <div class="graph-choice">
                    <label class="control control--radio">Radar<input type="radio" name="plotType" <?php if (isset($plotType) && $plotType=="Radar") echo "checked";?> value="Radar" class="button-primary" style="margin: 0;"><span class="control__indicator"></span></label>
            	</div>
                <div class="graph-choice">
                    <label class="control control--radio">Heat Map<input type="radio" name="plotType" <?php if (isset($plotType) && $plotType=="Heat Map") echo "checked";?> value="Heat Map" class="button-primary" style="margin: 0;"><span class="control__indicator"></span></label>
            	</div>
                <div class="graph-choice">
                    <label class="control control--radio">Ribbon<input type="radio" name="plotType" <?php if (isset($plotType) && $plotType=="Ribbon") echo "checked";?> value="Ribbon" class="button-primary" style="margin: 0;"><span class="control__indicator"></span></label>
            	</div>
                <div class="graph-choice">
                    <label class="control control--radio">Line<input type="radio" name="plotType" <?php if (isset($plotType) && $plotType=="Line") echo "checked";?> value="Line" class="button-primary" style="margin: 0;"><span class="control__indicator"></span></label>
            	</div>
                <input type="submit" name="submit" value="Generate" class="generate" style="color: green; padding: 5px 5px 0 8px;">
        </form>    
        </div>
        
              <!-- End Document
            –––––––––––––––––––––––––––––––––––––––––––––––––– -->
            </body>
</html>

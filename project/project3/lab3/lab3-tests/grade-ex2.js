var fs = require("fs");
var system = require("system");
var webpage = require("webpage");

var grading = require("./grading");

function main(studentDir) {
    if (studentDir === undefined) {
        console.log("USAGE: phantomjs " + system.args[0] + " student_dir/");
        phantom.exit();
        return;
    }
    var answerPath = studentDir + "/answer-2.html";
    if (!fs.isFile(answerPath)) {
        console.log("FAIL - No answer-2.html");
        phantom.exit();
        return;
    }

    grading.registerTimeout();

    // Initialize the world.
    grading.initUsers(function(auth) {
        // The grader (victim) will already be logged in to the zoobar
        // site before loading your page.
        phantom.cookies = auth.graderCookies;

        // Open the attacker's page.
        var page = webpage.create();

        // The location bar of the browser should not contain the
        // zoobar server's name or address at any point.
        page.onUrlChanged = function(targetUrl) {
            if (/^http:\/\/localhost:8080/.test(targetUrl)) {
                console.log("ERROR - Navigated to " + targetUrl);
            }
        };

	var target = "http://cseproj91.cse.iitk.ac.in:9443/";
        console.log("Loading attacker page. If you get a timeout here you're not redirecting to " + target + ".");
        page.open(answerPath);
        page.onLoadFinished = function(status) {
           console.log(page.url);
            if (page.url == target) {
                console.log("Visited final site.");
                page.onLoadFinished = null;
                page.close();

                // Check that the grader now has no zoobars.
                grading.getZoobars(function(number) {
                    if (number != 0) {
                        console.log("FAIL - grader has " + number + " zoobars, should have 0");
                    } else {
                        console.log("PASS - grader zoobar count");
                    }

                    // Check that the attacker now has 11.
                    phantom.cookies = auth.attackerCookies;
                    grading.getZoobars(function(number) {
                        if (number != 11) {
                            console.log("FAIL - attacker has " + number + " zoobars, should have 11");
                        } else {
                            console.log("PASS - attacker zoobar count");
                        }
                     	phantom.cookies = auth.attacker1Cookies;
                    	grading.getZoobars(function(number) {
                        	if (number != 19) {
                            		console.log("FAIL - attacker1 has " + number + " zoobars, should have 19");
                        	} else {
                            		console.log("PASS - attacker1 zoobar count");
                        	}
                        phantom.exit();
                        });
                });
            });
        }
    };
  });
}

main.apply(null, system.args.slice(1));

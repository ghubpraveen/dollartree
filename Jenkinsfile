node {
    // This displays colors using the 'xterm' ansi color map.
        stage('checkout') {
          checkout scm
        }
        stage('build') {
          sh 'zip pythonscript.zip app.py util.py'
        }
        stage('deploy') {
	  sh 'gsutil -m cp -r pythonscript.zip gs://dollartree'
        }
}

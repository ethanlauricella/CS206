<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="author" content="Emmanuel + Ethan">
        <title>Large 3</title>
        <meta name="description" content="This page is to use C++ to run and possibly display the GUI interface.">
        <link href="style.css" rel="stylesheet" type="text/css" media="screen" />
    </head>
    <body>
    	<header>
    		<h1>CS 120</h1>
            <h2>Soft Robot</h2>
    	</header>
        
        <?php
        
        $GenerationOptions = $_POST["GenerationOptions"];
        //echo "You chose the song " . $song;


        // Create a folder for the user where the processing will take place. It will be named a random number (so that it's different for each submission).
        $rand_number = rand();
        while (file_exists($rand_number)) {
            $rand_number = rand();
        }
        $command_mkdir = escapeshellcmd("mkdir " . $rand_number);
        $output_mkdir = shell_exec($command_mkdir);

        // Copy the files into the folder.

        $command_cp2 = escapeshellcmd("cp body.urdf " . $rand_number);
        $output_cp = shell_exec($command_cp2);

        $command_cp2 = escapeshellcmd("cp brain.nndf " . $rand_number);
        $output_cp = shell_exec($command_cp2);

        $command_cp2 = escapeshellcmd("cp constants.py " . $rand_number);
        $output_cp = shell_exec($command_cp2);

        $command_cp2 = escapeshellcmd("cp fitness.txt " . $rand_number);
        $output_cp = shell_exec($command_cp2);

        $command_cp2 = escapeshellcmd("cp generate.py " . $rand_number);
        $output_cp = shell_exec($command_cp2);

        $command_cp2 = escapeshellcmd("cp parallelHillClimber.py " . $rand_number);
        $output_cp = shell_exec($command_cp2);

        $command_cp2 = escapeshellcmd("cp motor.py " . $rand_number);
        $output_cp = shell_exec($command_cp2);

        $command_cp2 = escapeshellcmd("cp robot.py " . $rand_number);
        $output_cp = shell_exec($command_cp2);

        $command_cp2 = escapeshellcmd("cp search.py " . $rand_number);
        $output_cp = shell_exec($command_cp2);

        $command_cp2 = escapeshellcmd("cp sensor.py " . $rand_number);
        $output_cp = shell_exec($command_cp2);

        $command_cp2 = escapeshellcmd("cp simulate.py " . $rand_number);
        $output_cp = shell_exec($command_cp2);

        $command_cp2 = escapeshellcmd("cp simulation.py " . $rand_number);
        $output_cp = shell_exec($command_cp2);

        $command_cp2 = escapeshellcmd("cp solution.py " . $rand_number);
        $output_cp = shell_exec($command_cp2);

        $command_cp2 = escapeshellcmd("cp world.py " . $rand_number);
        $output_cp = shell_exec($command_cp2);

        $command_cp2 = escapeshellcmd("cp world.sdf " . $rand_number);
        $output_cp = shell_exec($command_cp2);

        $command_cp2 = escapeshellcmd("cp pyrosim/ " . $rand_number);
        $output_cp = shell_exec($command_cp2);

        $command_cp2 = escapeshellcmd("cp robot.cpp " . $rand_number);
        $output_cp2 = shell_exec($command_cp2);

        $command_cp2 = escapeshellcmd("cp numGen.txt " . $rand_number);
        $output_cp2 = shell_exec($command_cp2);

        $command_cp2 = escapeshellcmd("cp Final.txt " . $rand_number);
        $output_cp2 = shell_exec($command_cp2);

                $command_cp2 = escapeshellcmd("cp Data/ " . $rand_number);
        $output_cp2 = shell_exec($command_cp2);



        $output = shell_exec("cd " . $rand_number . ";g++ -std=c++1y -o robot.exe robot.cpp;./robot.exe " . $GenerationOptions . ";cd ..");

        #$output = shell_exec("cd " . $rand_number . "python search.py");


        // Print the output from the C++ program to the webpage.
        echo $output;
        
        // Delete the folder
        array_map("unlink", glob($rand_number . "/__pycache__/*"));
        rmdir($rand_number."/__pycache__");

        array_map("unlink", glob($rand_number . "/*"));
        rmdir($rand_number);

        ?>
        <p>Evolutionary Robotics simulation </p>
    </body>
</html>

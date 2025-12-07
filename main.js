const readline = require('readline');
const fs = require("fs");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

function main() {
    function loop() {
        rl.question(process.cwd() + " > ", (input) => {
            input = input.trim().toLowerCase();

            if (!input) {
                loop();
                return;
            }

            let parts = input.trim().split(" ");
            let cmd = parts[0].toLowerCase();
            let args = parts.slice(1);

            switch (cmd) {
                case "hello":
                    console.log(process.cwd() + " > Hello mate")
                    loop()
                    return;

                case "deldir":
                    let deld = args[0];

                    if (!deld) {
                        console.log(process.cwd() + " > Insert a name for delete a dir")
                        loop();
                        return;
                    }

                    try {
                        fs.rmdirSync(deld);
                        loop();
                        return;
                    } catch(err) {
                        console.log(process.cwd() + " > Error: " + err);
                        loop();
                        return;
                    }

                case "mv":
                    let source = args[0];
                    let destination = args[1]

                    if (!source || !destination) {
                        console.log(process.cwd() + " > Insert a valid source or destination!");
                        loop();
                        return;
                    }

                    try {
                        fs.renameSync(source, destination);
                        loop();
                        return;
                    } catch(err) {
                        console.log(process.cwd() + " > Error: " + err);
                        loop();
                        return;
                    }

                case "mkdir":
                    let tar = args[0];

                    if (!tar) {
                        console.log(process.cwd() + " > Insert a name for create a new dir")
                        loop();
                        return;
                    }

                    try {
                        fs.mkdirSync(tar);
                        loop();
                        return;
                    } catch(err) {
                        console.log(process.cwd() + " > Error: " + err);
                        loop();
                        return;
                    }

                case "cd":
                    let target = args[0]; 

                    if (!target) {
                        console.log(process.cwd() + " > Specify a directory!");
                        loop();
                        return;
                    }

                    try {
                        process.chdir(target);
                        loop();
                        return;
                    } catch(err) {
                        console.log(process.cwd() + " > Error: " + err);
                        loop();
                        return;
                    }

                case "mkfile":
                    let mkfil = args[0]; 

                    if (!mkfil) {
                        console.log(process.cwd() + " > Specify a filename!");
                        loop();
                        return;
                    }

                    try {
                        fs.writeFileSync(mkfil, "");
                        loop();
                        return;
                    } catch(err) {
                        console.log(process.cwd() + " > Error: " + err);
                        loop();
                        return;
                    }

                case "delfile":
                    let delfil = args[0]; 

                    if (!delfil) {
                        console.log(process.cwd() + " > Specify a filename!");
                        loop();
                        return;
                    }

                    try {
                        fs.unlinkSync(delfil);
                        loop();
                        return;
                    } catch(err) {
                        console.log(process.cwd() + " > Error: " + err);
                        loop();
                        return;
                    }

                case "ls":
                    fs.readdir(process.cwd(), (err, files) => {
                        if (err) {
                            console.error(process.cwd() + " > Error: " + err)
                            loop();
                            return;
                        }
                        files.forEach(file => console.log(file))
                        loop();
                        return;
                    })
                    loop();
                    return;

                case "exit":
                    console.log(process.cwd() + " > Goodbye mate <3")
                    rl.close();
                    return

                case "help":
                    console.log("Help -> All commands shown")
                    console.log("Hello -> return a welcome message")
                    console.log("ls -> View all files on the current dir")
                    console.log("cd -> move around the dirs with dir <dirname>")
                    console.log("mkdir -> create a dir with mkdir <dirname>")
                    console.log("deldir -> delete a dir with deldir <dirname>")
                    console.log("mkfile -> create a new file with mkfile <filename>")
                    console.log("delfile -> delete a file with delfile <filename>")
                    console.log("mv -> mv for move file with mv <filename> <destination/filename>")
                    console.log("exit -> for close the OS")
                    loop()
                    return;
                default:
                    console.log(process.cwd() + " > Unknown command, try a correct command or write 'help'")
                    loop()
                    return;
            }
        })
    }
    loop();
}

main();
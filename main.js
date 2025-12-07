const readline = require('readline');
const fs = require("fs");
const path = require("path");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

function main() {
    let history = [];

    function loop() {

        let before = process.cwd();
        let response = "MoneyOS";

        rl.question(before + " > ", (input) => {
            input = input.trim().toLowerCase();
            if (input != "history") {
                history.push(input);
            }

            if (!input) {
                loop();
                return;
            }

            let parts = input.trim().split(" ");
            let cmd = parts[0].toLowerCase();
            let args = parts.slice(1);

            switch (cmd) {
                case "hello":
                    console.log(response + " > Hello mate")
                    loop()
                    return;

                case "deldir":
                    let deld = args[0];

                    if (!deld) {
                        console.log(response + " > Insert a name for delete a dir")
                        loop();
                        return;
                    }

                    try {
                        fs.rmdirSync(deld);
                        loop();
                        return;
                    } catch(err) {
                        console.log(response + " > Error: " + err);
                        loop();
                        return;
                    }

                case "mv":
                    let source = args[0];
                    let destination = args[1]

                    if (!source || !destination) {
                        console.log(response + " > Insert a valid source or destination!");
                        loop();
                        return;
                    }

                    try {
                        if (fs.existsSync(destination) && fs.statSync(destination).isDirectory()) {
                            let filename = path.basename(source);
                            destination = path.join(destination, filename);
                        }

                        fs.renameSync(source, destination);
                        loop();
                        return;
                    } catch(err) {
                        console.log(response + " > Error: " + err);
                        loop();
                        return;
                    }

                case "mkdir":
                    let tar = args[0];

                    if (!tar) {
                        console.log(response + " > Insert a name for create a new dir")
                        loop();
                        return;
                    }

                    try {
                        fs.mkdirSync(tar);
                        loop();
                        return;
                    } catch(err) {
                        console.log(response + " > Error: " + err);
                        loop();
                        return;
                    }

                case "cd":
                    let target = args[0]; 

                    if (!target) {
                        console.log(response + " > Specify a directory!");
                        loop();
                        return;
                    }

                    try {
                        process.chdir(target);
                        loop();
                        return;
                    } catch(err) {
                        console.log(response + " > Error: " + err);
                        loop();
                        return;
                    }

                case "mkfile":
                    let mkfil = args[0]; 

                    if (!mkfil) {
                        console.log(response + " > Specify a filename!");
                        loop();
                        return;
                    }

                    try {
                        fs.writeFileSync(mkfil, "");
                        loop();
                        return;
                    } catch(err) {
                        console.log(response + " > Error: " + err);
                        loop();
                        return;
                    }

                case "delfile":
                    let delfil = args[0]; 

                    if (!delfil) {
                        console.log(response + " > Specify a filename!");
                        loop();
                        return;
                    }

                    try {
                        fs.unlinkSync(delfil);
                        loop();
                        return;
                    } catch(err) {
                        console.log(response + " > Error: " + err);
                        loop();
                        return;
                    }

                case "ls":
                    fs.readdir(process.cwd(), (err, files) => {
                        if (err) {
                            console.error(response + " > Error: " + err)
                            loop();
                            return;
                        }
                        files.forEach(file => console.log(file))
                        loop();
                        return;
                    })
                    return;

                case "exit":
                    console.log(response + " > Goodbye mate <3")
                    rl.close();
                    return

                case "cls":
                    for (let x = 0; x < 50; x++) {
                        console.log();
                    }
                    loop();
                    return;

                case "history":
                    for (let c of history) {
                        console.log(response + " > " + c);
                    }
                    loop();
                    return;

                case "write":
                    let filen = args[0];
                    let text = args.slice(1).join(" ");

                    if (!filen || !text) {
                        console.log(response + " > Insert a valid filename and text");
                        loop();
                        return;
                    }

                    try {
                        fs.writeFileSync(filen, text, { flag: "a" });
                        console.log(response + " > Text written successfully!");
                        loop();
                        return;
                    } catch(err) {
                        console.error(response + " > Error: " + err);
                        loop();
                        return;
                    }

                case "cat":
                    let catFile = args[0];

                    if (!catFile) {
                        console.log(response + " > Specify a filename!");
                        loop();
                        return;
                    }

                    try {
                        let content = fs.readFileSync(catFile, "utf-8");
                        console.log(content);
                        loop();
                        return;
                    } catch(err) {
                        console.log(response + " > Error: " + err);
                        loop();
                        return;
                    }

                case "open":
                    let openFile = args[0]; 

                    if (!openFile) {
                        console.log(response + " > Specify a filename!");
                        loop();
                        return;
                    }

                    try {
                        fs.openSync(openFile);
                        loop();
                        return;
                    } catch(err) {
                        console.log(response + " > Error: " + err);
                        loop();
                        return;
                    }

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
                    console.log("cls -> cls for clear the prompt")
                    console.log("history -> for view all history of command you used")
                    console.log("open -> for open a file with open <filename>")
                    console.log("cat -> for view the content of a file with cat <filename>")
                    console.log("write -> for write on a file with write <filename> <text>")
                    console.log("exit -> for close the OS")
                    loop()
                    return;
                default:
                    console.log(before + " > Unknown command, try a correct command or write 'help'")
                    loop()
                    return;
            }
        })
    }
    loop();
}

main();
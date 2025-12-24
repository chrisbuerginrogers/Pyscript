const { xworker } = document.getElementById("python-terminal");

xworker.sync.fred = async function (waitTime) {
    await new Promise(resolve => setTimeout(resolve, waitTime));
    return 23;
}


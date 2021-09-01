module.exports = async (github, context) => {
    const fs = require('fs').promises;
    const path = require('path');
    const upload_url = context.payload.release.upload_url;

    if (!upload_url) {
        throw "Missing release asset upload URL!";
    }

    for (let filePath of await fs.readdir('.')) {
        const fileExtension = path.extname(filePath);
        if (fileExtension != '.txt') {
            continue;
        }

        console.log(`Uploading '${filePath}'`);
        const contentLength = (await fs.stat(filePath)).size;
        const fileContents = await fs.readFile(filePath);
        await github.repos.uploadReleaseAsset({
            url: context.payload.release.upload_url,
            headers: {
                'content-type': 'application/octet-stream',
                'content-length': contentLength
            },
            name: path.basename(filePath),
            data: fileContents
        });
    }
};

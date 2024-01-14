const fs = require('fs');
const yaml = require('js-yaml');
const ncp = require('ncp').ncp;

// Read auto-assign.yml file
const autoAssignConfig = yaml.load(fs.readFileSync('.github/auto_assign.yml', 'utf8'));

// Update reviewers in auto-assign.yml
const reviewersInput = autoAssignConfig.reviewers;

// Rest of the script for creating the folder on the main branch
const mainFolderPath = 'src'; // 폴더를 생성할 경로

// 폴더가 없으면 생성
if (!fs.existsSync(mainFolderPath)) {
  fs.mkdirSync(mainFolderPath);
}

// 각 리뷰어에 대한 폴더 생성 및 파일 복사
reviewersInput.forEach((reviewer) => {
  const reviewerFolderPath = `${mainFolderPath}/${reviewer}`;

  if (!fs.existsSync(reviewerFolderPath)) {
    fs.mkdirSync(reviewerFolderPath, { recursive: true });
    console.log(`Folder created for ${reviewer} at ${reviewerFolderPath}`);

    // src/tiaz0128/ 아래의 전체 폴더 및 파일 복사
    const sourcePath = 'src/tiaz0128/';
    ncp(sourcePath, reviewerFolderPath, function (err) {
      if (err) {
        return console.error(err);
      }
      console.log(`Files and folders copied to ${reviewerFolderPath}`);
    });
  } else {
    console.log(`Folder for ${reviewer} already exists at ${reviewerFolderPath}`);
  }
});

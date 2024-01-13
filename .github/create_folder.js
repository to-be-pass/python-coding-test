const fs = require('fs');
const yaml = require('js-yaml');

// Read auto-assign.yml file
const autoAssignConfig = yaml.load(fs.readFileSync('.github/auto_assign.yml', 'utf8'));

// Update reviewers in auto-assign.yml
reviewersInput = autoAssignConfig.reviewers;

// Rest of the script for creating the folder on the main branch
const mainFolderPath = 'src'; // 폴더를 생성할 경로
// const studyFolderName = 'to-be';

// 폴더가 없으면 생성
if (!fs.existsSync(mainFolderPath)) {
  fs.mkdirSync(mainFolderPath);
}

// 각 리뷰어에 대한 폴더 생성
reviewersInput.forEach((reviewer) => {
  const reviewerFolderPath = `${mainFolderPath}/${reviewer}`;
  
  if (!fs.existsSync(reviewerFolderPath)) {
    fs.mkdirSync(reviewerFolderPath, { recursive: true });
    console.log(`Folder created for ${reviewer} at ${reviewerFolderPath}`);

    // 더미 파일 생성
    fs.writeFileSync(`${reviewerFolderPath}/.gitkeep`, '');
    console.log(`Dummy file added to ${reviewerFolderPath}`);
  } else {
    console.log(`Folder for ${reviewer} already exists at ${reviewerFolderPath}`);
  }
});
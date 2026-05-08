module.exports = {
  timeout: 30000,
  use: {
    headless: true,
    screenshot: "only-on-failure",
    trace: "off"
  },
  reporter: [["list"]]
};

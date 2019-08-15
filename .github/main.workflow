workflow "New workflow" {
  on = "push"
  resolves = ["HTTP client"]
}

action "HTTP client" {
  uses = "swinton/httpie.action@69125d73caa2c6821f6a41a86112777a37adc171"
  args = ["POST", "https://oapi.dingtalk.com/robot/send?access_token=401ba6382ba559299cd949bc478a3294eec519d96b6b95c9ba238322e1804ae1", "hello=world"]
}

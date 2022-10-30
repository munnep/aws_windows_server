output "windows_public-ip" {
  value = aws_eip.terraform_windows-eip.public_ip
}

output "windows_user" {
  value = "administrator"
}

output "windows_password" {
  value = rsadecrypt(aws_instance.windows_client.password_data, file("~/.ssh/id_rsa"))
}
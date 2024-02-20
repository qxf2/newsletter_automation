# load data from terraform output
content = inspec.profile.file('terraform.json')
params = JSON.parse(content)

PUBLIC_IP = params['instance_publicip']['value']
INTANCE_ID = params['instance_id']['value']
VPC_ID  = params['vpc_id']['value']

# chef inspec tests
#1
title "executing chef inspec tests"
describe aws_ec2_instance(name: 'docker-EC2instance') do
    it { should exist }
end
#2
describe aws_ec2_instance(INTANCE_ID) do
    it { should be_running }
    its('instance_type') { should eq 't2.micro' }
    its('image_id') { should eq 'ami-fa2fb595' }
end
#3
describe aws_vpc(vpc_id: VPC_ID) do
    its('cidr_block') { should cmp '10.0.0.0/16' }
end
#4
describe aws_security_group(group_name: 'docker_sg') do
    it { should exist }
    its('group_name') { should eq 'docker_sg' }
    its('description') { should eq 'Security group for Docker EC2 instance' }
    its('vpc_id') { should eq VPC_ID }  
end
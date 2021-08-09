"""
This is an example automated test to help you learn Qxf2's framework
Our automated test will do the following:
    #Open tests main page.
    #Check URL
"""
import os,sys,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
from utils.Option_Parser import Option_Parser
import conf.check_current_url_conf as conf

def test_check_current_url(base_url,browser,browser_version,os_version,os_name,remote_flag,remote_project_name,remote_build_name):
    "Run the test"
    try:
        #Initialize flags for tests summary
        expected_pass = 0
        actual_pass = -1

        #1. Create a test object and fill the example form.
        test_obj = PageFactory.get_page_object("Main Page",base_url=base_url)

        #2. Setup and register a driver
        start_time = int(time.time())	#Set start_time with current time
        test_obj.register_driver(remote_flag,os_name,os_version,browser,browser_version,remote_project_name,remote_build_name)
        
        #3. Get the test details from the conf file
        url = conf.url

        #4. Verify current url
        current_url = test_obj.get_URL() 
        result_flag = False
        print("url:",current_url)
        if url in current_url:
            result_flag = True

        test_obj.log_result(result_flag,
                            positive="Landed on correct URL: %s\n"%url,
                            negative="Failed to land on correct url: %s \n Landed at url: %s"%(url,current_url))
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        
        #Check page header
        result_flag = test_obj.check_page_header()
        test_obj.log_result(result_flag,
                            positive="Header check was successful\n",
                            negative="Header looks wrong.\nObtained the header %s\n"%test_obj.get_page_header())
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))        

        #5. Print out the results
        test_obj.write_test_summary()

        #Teardown
        test_obj.wait(3)
        expected_pass = test_obj.result_counter
        actual_pass = test_obj.pass_counter
        test_obj.teardown()
        
    except Exception as e:
        print("Exception when trying to run test:%s"%__file__)
        print("Python says:%s"%str(e))

    assert expected_pass == actual_pass, "Test failed: %s"%__file__
       
    
#---START OF SCRIPT   
if __name__=='__main__':
    print("Start of %s"%__file__)
    #Creating an instance of the class
    options_obj = Option_Parser()
    options = options_obj.get_options()
                
    #Run the test only if the options provided are valid
    if options_obj.check_options(options): 
        test_check_current_url(base_url=options.url,
                        browser=options.browser,
                        browser_version=options.browser_version,
                        os_version=options.os_version,
                        os_name=options.os_name,
                        remote_flag=options.remote_flag,
                        remote_project_name=options.remote_project_name,
                        remote_build_name=options.remote_build_name) 
    else:
        print('ERROR: Received incorrect comand line input arguments')
        print(options_obj.print_usage())

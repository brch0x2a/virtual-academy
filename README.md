# virtual-academy

## FE Details

- ### Importing files

  - **_The following way to import files in frontend is necessary due to the dependency resolution process that Flask provides._**

  1.  **_First of all be sure to add the following HTML code in your view:_**

  ```HTML
  <script type="text/javascript" src="{{ url_for('static', filename='js/scriptImporter.js') }}" ></script>
  ```

  2. **_For readability and order purposes be sure to add all your code in a function like the following:_**

  ```JAVASCRIPT
  function descriptiveName(){
      // Here i will execute code that requires external functions or processes that usually goes outside a function.
  }
  ```

  3. **_Then import all your files with the following format, note that the function is executed after the document is ready, this is made to avoid problems with asynchronous importing:_**

  ```JAVASCRIPT
  $( document ).ready(
      function(){
          importScript('nameOfTheFile'); // First import
          importScript('nameOfTheOtherFile'); // Second import
          // Last import, in this be sure to send as second parameter your function
          importScript('lastFileName',myFunctionWithDescriptiveName);
          // myFunctionWithDescriptiveName is executed as a callback function
  });
  ```

  4. **_Now you are ready to destroy the world_**

- ### Using generalized JQuery calls

- Here we have 2 cases to address, but first let's take a look on generalized JQuery functions:
  Let's take as example function `getCourseByCategoryId` **:**

  ```JAVASCRIPT
  function getCourseByCategoryId(categoryId,callBackFunction){
      $.getJSON("getCourseBy?"+"categoryId="+categoryId, data =>{
          callbackHandler(callBackFunction, data);
      });
  }
  ```

  - Note the following details:
    - Here we use the first parameter to fed the getJSON operation.
    - Second parameter is a callback function that we redirect to a callback handler to avoid the effort of knowing the callback function specifications.
        - Callback handler will take care of giving data and others parameters to our callback function.
    - We call the callback handler giving callback function as first parameter and data (obtained from getJSON operation) as second parameter.
    - We will call `getCourseByCategoryId` using the following pattern:
        ```JAVASCRIPT
        getCourseByCategoryId(categoryId,ourCallBackFunction);
        // CASE #1
        ```
        Or
        ```JAVASCRIPT
        getCourseByCategoryId(categoryId,function(data){
            ourCallBackFunction(requiredParameters,data);
        });
        // CASE #2
        ```
    - On the first case we are facing a simple scenario where our callback function just need a single parameter, those are simple, we just need to pass callback Function as parameter.
    
    - On the second case we need to pass to our callback function parameters that our getJSON operation can not and could not calculate or know ***(Remember single responsibility)***, for that case we define a transitory function that will help us to pass our parameters in a clean way and callback handler will take care of that function.


- ### Files content standard (TODO)

- ### Files naming standard (TODO)

## Environment Details

### To activate virtual eviroment run

```Bash
    source venv/bin/activate

```

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

- ### Files content standard (TODO)

- ### Files naming standard (TODO)

## Environment Details

### To activate virtual eviroment run

```Bash
    source venv/bin/activate

```

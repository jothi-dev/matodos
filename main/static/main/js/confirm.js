
window.confirmTodoDelete = function(todo_id, elem) {
    // the confirm funtion will return true if the user clicks `ok`, and false if `cancel` is clicked on the prompt
    if (confirm("Are you sure you WANT to do this?")) {
        // we want to delete a specific todo so we need to add the id to the url 
        elem.href = `/delete/todo/${todo_id}`
        // submit will now send the delete request
        elem.submit()
    }
}

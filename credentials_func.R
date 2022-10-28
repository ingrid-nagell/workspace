getCredentials = function(targetMachine){
  netrcFile <- file.path(path.expand("~"), ".netrc", fsep = .Platform$file.sep)
  con = file(netrcFile, "r")
  # read whole (small) file into a single string, collape any newlines
  netrcStr <- paste(readLines(con), collapse=" ")
  close(con)
  # split the fields on whitespace (.netrc format can be 1 line per host or multiline)
  fields <- strsplit(netrcStr, "\\s+")[[1]]
  machine <- ''
  username <- ''
  password <- ''
  i=1
  while (i <= length(fields)) {
    # process the fields
    if (fields[i] == 'machine') {
      i <- i +1
      machine <- fields[i]
      username <- ''
      password <- ''
      i <- i +1
    } else if (fields[i] == 'default') {
      i <- i +1
      machine <- 'default'
    } else if (fields[i] == 'login') {
      i <- i +1
      username <- fields[i]
      i <- i +1
    } else if (fields[i] == 'password') {
      i <- i +1
      password <- fields[i]
      i <- i +1
    } else {
      i <- i + 1
    }
    if ((machine == targetMachine || machine == 'default') &&
        (username != '') && (password != '') ) {
      break
    }
  }
  return (list("username" = username, "password" = password))
}
# example use
credentials <- getCredentials('db2')


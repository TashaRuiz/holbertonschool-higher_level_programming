# Basics of HTTP/HTTPS

---

## 1. Differences between HTTP and HTTPS
**HTTP (Hypertext Transfer Protocol)** is the basic protocol that allows browsers (clients) to request resources from web servers and receive responses. Data travels in **plain text**.

**HTTPS (HTTP Secure)** is the same protocol with an added security layer using **SSL/TLS encryption**.

### Main differences (focusing on security):
| **Aspect**      | **HTTP**                    | HTTPS                                                      |
|-----------------|-----------------------------|------------------------------------------------------------|
| Security        | No encryption               | Encrypted with SSL/TLS                                     |
| Data visibility | Anyone can read the data    | Data is unreadable to eavesdroppers                        |
| Integrity       | Can be modified in transit  | Detects tampering                                          |
| Authentication  | No server verification      | Server identity verified via certificates                  |
| Default port    | 80                          | 443                                                        |
| URL prefix      | http://                     | https://                                                   |
| Typical use     | Simple, non-sensitive sites | Login pages, banking, email, e-commerce, most modern sites |

### Key takeaway:
>The “S” stands for Secure. HTTP sends everything (including passwords and cookies) in clear text. HTTPS encrypts the entire communication so that even if someone intercepts the traffic, they cannot read or alter it. Websites that handle sensitive data almost always use HTTPS.


## 2. Structure of an HTTP Request and Response
Both requests and responses share a similar structure:
1. **Start line** (single line)
2. **Headers** (zero or more lines of metadata)
3. **Blank line** (marks the end of headers)
4. **Optional body** (the actual data)

### HTTP Request structure:
```Text
GET /index.html HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Accept: text/html
Accept-Language: en-US
```
- **Start line (Request line):**
    Method + Path/URL + HTTP version
    Example: GET /index.html HTTP/1.1

- **Headers:**
    Key-value pairs that provide extra information
    (e.g., Host, User-Agent, Content-Type, Authorization, etc.)

- **Blank line**

- **Body (optional):** 
    Used mainly with methods like POST or PUT (form data, JSON, file uploads, etc.)

### HTTP Response structure:
```Text
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1234
Date: Fri, 13 Nov 2026 09:00:00 GMT

<!DOCTYPE html>
<html>...</html>
```
- **Start line (Status line):**
    HTTP version + Status code + Reason phrase
    Example: HTTP/1.1 200 OK

- **Headers:**
    Information about the response
    (e.g., Content-Type, Content-Length, Set-Cookie, Cache-Control)

- **Blank line**

- **Body (optional):**
    The actual content (HTML page, JSON data, image, etc.)


## 3. Common HTTP Methods (at least 4)
| **Method**    | **Description**                                           | **Typical Use Case**                                              |
|---------------|-----------------------------------------------------------|-------------------------------------------------------------------|
| GET           | Retrieves a resource from the server                      | Loading a web page, fetching data from an API                     |
| POST          | Submits data to the server (often creates something new)  | Submitting a form, creating a new user/account, uploading a file  |
| PUT           | Replaces/updates an entire resource                       | Updating a full user profile or document                          |
| DELETE        | Deletes a specified resource                              | Removing a post, account, or file                                 |
| PATCH (bonus) | Partially updates a resource                              | Changing only one field (e.g., updating just the email)           |
| HEAD (bonus)  | Same as GET but without the response body                 | Checking if a resource exists or getting metadata only            |


## 4. Common HTTP Status Codes (5 examples)
Status codes are grouped by the first digit:
   * **1xx** → Informational
   * **2xx** → Success
   * **3xx** → Redirection
   * **4xx** → Client error
   * **5xx** → Server error

| **Status Code**           | **Description**                                            | **Scenario / When you might see it**                       |
|---------------------------|------------------------------------------------------------|------------------------------------------------------------|
| 200 OK                    | Request succeeded                                          | Successfully loading a webpage or receiving API data       |
| 301 Moved Permanently     | Resource has a new permanent URL                           | Website redirects from old URL to a new one (SEO-friendly) |
| 404 Not Found             | Requested resource does not exist                          | Typing a wrong URL or requesting a deleted page            |
| 500 Internal Server Error | Server encountered an unexpected error                     | Bug in the server code or misconfigured server             |
| 403 Forbidden             | Server understood the request but refuses to authorize it  | Trying to access a restricted page without permission      |

### Extra useful ones:
* **201 Created** → Resource successfully created (common after POST)
* **401 Unauthorized** → Authentication required / failed
* **302 Found** → Temporary redirect

---

## Author
>Developed by Tasha Arroyo, a Holberton School student 
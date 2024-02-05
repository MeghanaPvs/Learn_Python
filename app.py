from flask import Flask
app = Flask(__name__) #created an instance to this server

#defining routes:
#test route
@app.route('/test', methods=['GET'])
def test():
    return "Hello, This is a test route"
# To test this route : http://127.0.0.1:3000/


# Sample data
posts = [
    {'id': 1, 'title': 'Post 1', 'content': 'This is the content of post 1'},
    {'id': 2, 'title': 'Post 2', 'content': 'This is the content of post 2'}
]
#Create operation
@app.route('/post/create', methods=['POST'])

def create_post():
    new_post = {'id': len(posts) + 1, 'title': 'New Post', 'content': 'This is a new post'}
    posts.append(new_post)
    return {'message': 'Post created successfully', 'post': new_post}

# Read operation
@app.route('/posts')
def get_posts():
    return {'posts': posts}
if __name__ == '__main__':
    app.run(debug=True,port=3000)

from distutils.core import setup

if __name__ == "__main__":
    setup(name="mongauth", 
          packages=["."],
          version="1.0.1", 
          author="Moses Nakamura", 
          author_email="nnythm@gmail.com",
          url="https://github.com/mnn2104/mongauth", 
          description="User Authentication with MongoDB", 
          long_description="""
          PyMongo + Authentication  Super simple.
          Super fun.
          Uses the bcrypt library to be very, very secure.
          Will not store any other user data, by design.
          You can keep that stuff elsewhere.""",
          classifiers=["Programming Language :: Python",
                       "License :: OSI Approved :: Apache Software License",
                       "Operating System :: OS Independent",
                       "Development Status :: 4 - Beta",
                       "Environment :: Web Environment",
                       "Intended Audience :: Developers",
                       "Topic :: Software Development :: Libraries :: Python Modules",
                       "Topic :: Database :: Database Engines/Servers",
                       "Topic :: Security :: Cryptography",
                       "Topic :: System :: Systems Administration :: Authentication/Directory"]
          )

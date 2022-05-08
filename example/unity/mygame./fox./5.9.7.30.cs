using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class playerController : MonoBehaviour
{
    public Rigidbody2D rb;
    public float speed;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        Movement();
    }

    void Movement()
    {
        float horizontalMove=Input.GetAxis("Horizontal");
        float facedirection = Input.GetAxisRaw("Horizontal");

        if(horizontalMove !=0)
        {
            rb.velocity=new Vector2(horizontalMove*speed,rb.velocity.y);

        }

        if(facedirection !=0)
        {
            rb.transform.localScale=new Vector3(horizontalMove,1,1);

        }

    }
}
